from aiohttp import web
from aiohttp_swagger import setup_swagger


async def welcome(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)
