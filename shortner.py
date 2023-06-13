import logging
import asyncio
import aiohttp
from config import WEBSITE, API

async def get_shortlink(link):
    https = link.split(":")[0]
    if "http" == https:
        https = "https"
        link = link.replace("http", https)
    url = f'https://{WEBSITE}/api'
    params = {'api': API,
              'url': link,
              }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, raise_for_status=True, ssl=False) as response:
                data = await response.json()
                if data["status"] == "success":
                    return data['shortenedUrl']
                else:
                    logger.error(f"Error: {data['message']}")
                    return f'https://{WEBSITE}/api?api={API}&link={link}'

    except Exception as e:
        logger.error(e)
        return f'https://{WEBSITE}/api?api={API}&url={link}'
