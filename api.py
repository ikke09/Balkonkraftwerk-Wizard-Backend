from werkzeug import exceptions
from flask import Flask, request
import os
from coords import get_coords

from models import BalconyModel, VersionModel
from balcony_metadata import extract_metadata

from dotenv import load_dotenv
load_dotenv()


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
        return {
            'status': 400,
            'message': f'{e}',
        }

    @app.get("/api")
    def version():
        return VersionModel().json()

    @app.get("/api/coords")
    def coords():
        zip_param = request.args.get('zip')
        if not zip_param:
            raise exceptions.BadRequest("zip param missing!")
        city = request.args.get('city')
        if not city:
            raise exceptions.BadRequest("city param missing!")
        zip = int(zip_param)
        coordinates = get_coords(zip, city)
        if coordinates is None:
            raise exceptions.BadRequest(
                f"Could not retrieve coordinates for {zip}")
        return coordinates.json()

    @app.post("/api/balcony")
    def balcony():
        data = request.get_json()
        balcony = BalconyModel(data)
        if balcony.base64 == '':
            raise exceptions.BadRequest("Image must be encoded as base64")
        res = extract_metadata(balcony=balcony)
        if res is None:
            raise exceptions.BadRequest("Image could not be processed")
        return res.json()

    @app.post("/api/kpi")
    def kpi():
        return "<p>Hello, World!</p>"

    return app
