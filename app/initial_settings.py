from typing import NoReturn

from flask import Flask


class InitialSettings:
    def __init__(self, app: Flask):
        self.app = app

    def blueprint_registration(self) -> NoReturn:
        # blueprint for auth routes
        from app.routes.main import main as main_blueprint
        self.app.register_blueprint(main_blueprint)
        from app.routes.api import api as api_blueprint
        self.app.register_blueprint(api_blueprint)

    def error_handlers(self):
        # Import HTTP base error handlers
        pass
