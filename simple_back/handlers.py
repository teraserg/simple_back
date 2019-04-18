from aiohttp import web
import logging

logger = logging.getLogger(__name__)


async def index(request):
    text = "This is Simple Back"
    logger.info(text)
    return web.Response(text=text)


async def health_check(request):
    text = "Health check"
    logger.debug(text)
    return web.Response(text=text)


async def welcome(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    logger.debug(text)
    return web.Response(text=text)


async def log_msg(request):
    log_msg = request.match_info.get('log_msg', "nothing")
    logger.debug(log_msg)
    return web.Response(text=log_msg)
