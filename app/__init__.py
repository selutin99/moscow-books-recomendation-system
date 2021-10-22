from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_sessionstore import Session

from app.config.profiles import DevConfig, ProdConfig
from app.utils.db_utils.pymysql_db_provider import PyMySQLProvider
from app.initial_settings import InitialSettings
from app.utils.flask_inject import Inject

# Create Flask application object and
app = Flask(__name__)
active_profile = ProdConfig()

# Dependency injection container
injector = Inject(app)

# Database connect providers
db = SQLAlchemy()
pymysql_db = PyMySQLProvider(active_profile=active_profile)


def create_app() -> Flask:
    init_settings: InitialSettings = dependency_injection_container_initialize()
    # Function for registration blueprints of routes in app
    init_settings.blueprint_registration()
    # Import error handlers
    init_settings.error_handlers()

    Session(app)

    db.init_app(app)

    return app


def dependency_injection_container_initialize() -> InitialSettings:
    from app.services.container import container as ioc_container
    ioc_container()
    return injector.get('init_settings')
