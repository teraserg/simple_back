from aiohttp import web
from aiohttp_swagger import setup_swagger
from simple_back.logger import get_logger
logger = get_logger(__name__)


async def welcome(request):
    logger.debug('welcome handler')
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)
