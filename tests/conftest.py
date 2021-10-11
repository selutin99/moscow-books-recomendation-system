import pytest
from flask import Flask

from app import create_app


@pytest.fixture(scope='module')
def test_client():
    flask_app: Flask = create_app()

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client
