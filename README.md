# async_ocrspace

A Python asynchronous wrapper for [ocr.space API](https://ocr.space/OCRAPI)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install async-ocrspace.

```bash
pip install async_ocrspace
```

## Usage

```python
import asyncio
from async_ocrspace import AsyncOCRSpace


async def main():
    image_url = 'Image'
    table_image_url = 'Image of a table'
    base64_image = 'data:image/png;base64....'
    api = AsyncOCRSpace(api_key='helloworld', OCREngine='2', scale='true')
    first_task = api.fetch_ocr_by_url(image_url)
    second_task = api.fetch_ocr_by_url(table_image_url, isTable='true', language='chs', OCREngine ='1')
    third_task = api.fetch_ocr_by_base64image(base64_image)
    results = await asyncio.gather(first_task, second_task, third_task) # returns a list of JSON responses
    print(results)
    await api.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

```