from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
ma = Marshmallow(app)


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://tomato:123456@localhost:5432/ripe_tomatoes_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


## DB CONNECTION AREA
db = SQLAlchemy(app)


# CLI COMMANDS AREA
@app.cli.command("create")
def create_table():
  db.create_all()
  print("Tables created")


@app.cli.command("drop")
def drop_table():
  db.drop_all()
  print("Tables dropped")


@app.cli.command("seed")
def seed_tables():
  movie1 = Movies(
    title = "The Dark Knight",
    genre = "Action",
    length = 152,
    year = 2008
  )
  movie2 = Movies(
    title = "Thor: Love and Thunder",
    genre = "Action",
    length = 118,
    year = 2022
  )
  actor1 = Actors(
    first_name = "Christian",
    last_name = "Bale",
    gender = "Male",
    country = "UK",
    dob = "30/01/1974"
  )
  actor2 = Actors(
    first_name = "Chris",
    last_name = "Hemsworth",
    gender = "Male",
    country = "AUS",
    dob = "11/08/1983"
  )
  actor3 = Actors(
    first_name = "Michael",
    last_name = "Caine",
    gender = "Male",
    country = "UK",
    dob = "14/03/1933"
  )
  db.session.add_all([movie1, movie2, actor1, actor2, actor3])
  db.session.commit()
  print("Tables seeded")


# MODELS AREA
class Movies(db.Model):
  __tablename__ = "movies"

  id = db.Column(db.Integer, primary_key = True)

  title = db.Column(db.String())
  genre = db.Column(db.String())
  length = db.Column(db.Integer)
  year = db.Column(db.Integer)


class Actors(db.Model):
  __tablebame__ = "actors"
  
  id = db.Column(db.Integer, primary_key = True)

  first_name = db.Column(db.String())
  last_name = db.Column(db.String())
  gender = db.Column(db.String())
  country = db.Column(db.String())
  dob = db.Column(db.String())


# SCHEMAS AREA
class MovieSchema(ma.Schema):
  class Meta:
    fields = ("id", "title", "genre", "length", "year")

class ActorSchema(ma.Schema):
  class Meta:
    fields = ("id", "first_name", "last_name", "gender", "country", "dob")


movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)
actor_schema = ActorSchema()
actors_schema = ActorSchema(many=True)

# ROUTING AREA

@app.route("/")
def hello():
  return "Welcome to Ripe Tomatoes API"

@app.get("/movies")
def get_movies():
  stmt = db.select(Movies)
  movies = db.session.scalars(stmt)
  result = movies_schema.dump(movies)
  return jsonify(result)


@app.get("/actors")
def get_actors():
  stmt = db.select(Actors)
  actors = db.session.scalars(stmt)
  result = actors_schema.dump(actors)
  return jsonify(result)