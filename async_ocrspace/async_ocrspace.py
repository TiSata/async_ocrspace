import aiohttp
import asyncio


class AsyncOCRSpace:
    def __init__(self, api_url='http://api.ocr.space/parse/image', api_key='helloworld', **payload):
        self._session = aiohttp.ClientSession()
        self.api_url = api_url
        self.header = {'apiKey': api_key}
        self.payload = payload

    async def _fetch(self, data, **payload):
        for name, value in {**self.payload, **payload}.items():
            data.add_field(name, value)
        async with self._session.post(self.api_url, data=data, headers=self.header) as resp:
            return await resp.json()

    async def fetch_ocr_by_url(self, url: str, **payload):
        data = aiohttp.FormData()
        data.add_field('url', url)
        return await self._fetch(data, **payload)

    async def fetch_ocr_by_file(self, filename: str, **payload):
        data = aiohttp.FormData()
        data.add_field('file', open(filename, 'rb'), filename=filename)
        return await self._fetch(data, **payload)

    async def fetch_ocr_by_base64image(self, base64image, **payload):
        data = aiohttp.FormData()
        data.add_field('base64Image', base64image)
        return await self._fetch(data, **payload)

    async def close(self):
        await self._session.close()
        self._session = None
