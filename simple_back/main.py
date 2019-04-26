import pathlib
from aiohttp import web
from aiohttp_swagger import setup_swagger
from simple_back import handlers
from simple_back import utils, settings
import simple_back.db.manager as db_manager


THIS_DIR = pathlib.Path(__file__).parent
ENV_LOCAL = 'local'
ENV_LOCAL_DOCKER = 'local_docker'


def setup_routes(app):
    app.router.add_get('/', handlers.welcome)
    app.router.add_get('/{name}', handlers.welcome)
    app.router.add_get('/db/version', handlers.db_version)


async def startup(app: web.Application):
    print(f'startup {app.name}')

    if settings.ENV == ENV_LOCAL_DOCKER:
        db_config = db_manager.DBConfigPostgresLocalDocker()
    else:
        db_config = db_manager.DBConfigPostgresLocal()

    app.db_engine = db_manager.SqlAlchemyPostgresDBEngine(db_config)
    print(f'db engine: {app.db_engine}')


async def cleanup(app: web.Application):
    print(f'cleanup {app.name}')


@web.middleware
async def error_handler_middleware(request, handler):
    # request_path = request.path
    # request_handler_name = request.match_info.handler.__name__

    try:
        response = await handler(request)
    except web.HTTPClientError:
        raise
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
