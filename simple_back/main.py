import pathlib
from aiohttp import web
from aiohttp_swagger import setup_swagger
from simple_back import handlers
from simple_back import utils


THIS_DIR = pathlib.Path(__file__).parent


def setup_routes(app):
    app.router.add_get('/', handlers.welcome)
    app.router.add_get('/{name}', handlers.welcome)


async def startup(app: web.Application):
    print(f'startup {app.name}')
    pass


async def cleanup(app: web.Application):
    print(f'cleanup {app.name}')
    pass


@web.middleware
async def error_handler_middleware(request, handler):
    # request_path = request.path
    # request_handler_name = request.match_info.handler.__name__

    try:
        response = await handler(request)
    except Exception as e:
        traceback_str = utils.exception_traceback_str(e)
        return web.HTTPServiceUnavailable(reason=traceback_str)

    return response


def create_app():
    app = web.Application(
        middlewares=[error_handler_middleware]
    )
    app.name = 'simple_back'
    setup_routes(app)

    swagger_file = THIS_DIR / 'swagger.yml'
    setup_swagger(app, swagger_from_file=swagger_file)

    app.on_startup.append(startup)
    app.on_cleanup.append(cleanup)

    return app


def main():
    print("Hello World!")
    app = create_app()
    web.run_app(app)


if __name__ == "__main__":
    main()
