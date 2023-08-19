from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
ma = Marshmallow(app)


# set database URI via SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://db_dev:123456@localhost:5432/trello_clone_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# create the database object
db = SQLAlchemy(app)


# CLI Command Area
@app.cli.command("create")
def create_table():
    db.create_all()
    print("Tables created")


@app.cli.command("seed")
def seed_table():
    from datetime import date
    card1 = Card(
        #set all attributes except the id
        title = "Start the project",
        description = "Stage 1, creating the database",
        date = date.today(),
        status = "To Do",
        priority = "High"
    )
    db.session.add(card1)

    card2 = Card(
        title = "SQLAlchemy and Marshmallow",
        description = "Stage 2, integrate both modules in the project",
        date = date.today(),
        status = "Ongoing",
        priority = "High"
    )
    db.session.add(card2)
    db.session.commit()
    print("Table seeded")

@app.cli.command("drop")
def drop_table():
    db.drop_all()
    print("Tables dropped")


# Model Area
class Card(db.Model):
    # define the table
    __tablename__ = "cards"
    # Set primary key
    id = db.Column(db.Integer, primary_key = True)
    # Add other attributes
    title = db.Column(db.String())
    description = db.Column(db.String())
    date = db.Column(db.Date())
    status = db.Column(db.String())
    priority = db.Column(db.String())
    

# Schema Area
class CardSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "description", "date", "status", "priority")

card_schema = CardSchema()
cards_schema = CardSchema(many=True)


# Routing Area
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/cards", methods=["GET"])
def get_cards():
    stmt = db.select(Card)
    cards = db.session.scalars(stmt)
    result = cards_schema.dump(cards)
    return jsonify(result)