from aiohttp import web
from aiohttp_swagger import setup_swagger


async def welcome(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


async def db_version(request):
    db_engine = request.app.db_engine
    db_v = db_engine.version()
    return web.Response(text=f'DB VERSION: {db_v}')
