from flask import Flask
from flask_restful import Api

app = Flask(__name__)


def run(host, port):
    api = Api(app=app, prefix='/v1')
    _configure_routes(api)
    app.run(host, port, load_dotenv=True)


def _configure_middlewares(api: Api):
    pass


def _configure_routes(api: Api):
    from .resources import pets
    api.add_resource( pets.Pets, "/pets")
