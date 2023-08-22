from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    # using a list comprehension and multiple assignment
    # to grab the environment variable we need

    # Creating the flask app object - this is the core of the app
    app = Flask(__name__)

    # configuring the app
    app.config.from_object("config.app_config")

    # create our database object, allowing use of ORM
    db.init_app(app)

    # creating our marshmallow object, allows us to use schemas
    ma.init_app(app)

    #import the controllers and activate the blueprints
    from controllers import registerable_controllers

    for controller in registerable_controllers:
        app.register_blueprint(controller)

    return app