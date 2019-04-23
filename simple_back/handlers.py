from aiohttp import web
from simple_back.logger import get_logger
logger = get_logger()


async def welcome(request):
    logger.debug('welcome handler')
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


async def health_check(request):
    logger.debug('health check')
    return web.Response(text='ok')
