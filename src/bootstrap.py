import imp
import os

from  connexion import FlaskApp, RestyResolver
from flask import Flask

from .healthcheck import healthcheck_blueprint

class Bootstrap:
    def __init__(self) -> None:
        self.application = Flask

    def init_app(self) -> Flask:
        self.path = os.path.abspath("")
        # options = {'swagger_url': '/'}
        options = {'swagger_url': '/'}
         
        connexion_app = FlaskApp(__name__)
        connexion_app.add_api('swagger.yml', arguments={'title': 'RestyResolver Example'}, resolver=RestyResolver('api'))
        self.application = connexion_app.app

    def create_app(self):
        self.init_app()
        self.application.register_blueprint(healthcheck_blueprint)

    def run(self):
        self.create_app()
        self.application.run()