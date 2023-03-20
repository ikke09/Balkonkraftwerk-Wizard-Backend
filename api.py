from werkzeug import exceptions
from flask import Flask, request
import os

from models import BalconyModel, VersionModel
from balcony_metadata import extract_metadata

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        ENV='dev',
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.errorhandler(exceptions.BadRequest)
    def handle_bad_request(e):
        return 'bad request!', 400

    @app.get("/api")
    def version():
        return VersionModel().json()

    @app.post("/api/balcony")
    def balcony():
        data = request.get_json()
        balcony = BalconyModel(data)
        return extract_metadata(balcony=balcony).json()

    @app.post("/api/kpi")
    def kpi():
        return "<p>Hello, World!</p>"

    return app
