import asyncio
import aiohttp
import logging

logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')

async def get_speed_with_download(url, session):
    try:
        logging.debug(f"Starting to fetch data from {url}")
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.text()
                logging.debug(f"Successfully fetched data from {url}")
                # 这里需要根据实际情况解析数据，假设返回的是一个包含 'url' 键的字典
                # 目前简单返回一个示例结果，实际需要根据返回数据调整
                result = {'url': url}
                return result
            else:
                logging.warning(f"Failed to fetch data from {url}. Status code: {response.status}")
                return None
    except Exception as e:
        logging.error(f"Error occurred while fetching data from {url}: {e}", exc_info=True)
        return None
    
