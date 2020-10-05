from flask import Flask
from flask_restful import Api
from frameworks_and_drivers.storage.inmemory.repositories \
    import users_inmemory_repository as users_repository

app = Flask(__name__)


def run(host, port):
    api = Api(app=app, prefix='/v1')
    _configure_middlewares(api, app)
    _configure_routes(api)
    app.run(host, port, load_dotenv=True, debug=True)


def _config(app: Flask):
    """
    setup config app
    """
    app.config['SECRET_KEY'] = 'super-secret'


def _configure_middlewares(api: Api, app: Flask):
    from .middlewares import auth
    auth.setup(app, users_repository.UsersInMemoryRepository())


def _configure_routes(api: Api):
    from .resources import pets, health
    api.add_resource(health.Health, '/health')
    api.add_resource(pets.Pets, '/pets')
