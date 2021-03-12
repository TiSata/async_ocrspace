import aiohttp


class AsyncOCRSpace:
    API_URL = 'http://api.ocr.space/parse/image'  # Free tier url

    def __init__(self, api_key, api_url=API_URL, **payload):
        self._session = aiohttp.ClientSession(headers={'apiKey': api_key})
        self.api_url = api_url
        self.payload = payload

    async def _fetch(self, data, **payload):
        for name, value in {**self.payload, **payload}.items():
            data.add_field(name, value)
        async with self._session.post(self.api_url, data=data) as resp:
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
