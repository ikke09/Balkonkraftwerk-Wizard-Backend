import os
from pathlib import Path
from flask import Flask, request
from werkzeug import exceptions
from models import BalconyModel, VersionModel


def create_app():
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent
    UPLOAD_FOLDER = os.path.join(os.path.dirname(BASE_DIR), 'images')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    return app


app = create_app()


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
    return balcony.json()


@app.post("/api/kpi")
def kpi():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run()
