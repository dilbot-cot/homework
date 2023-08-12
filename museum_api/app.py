from flask import Flask, abort
import json

app = Flask(__name__)

# Need to have some data to return.
# For a production app this information would be stored in a database of course...
art_dict = {
    "composition 8": {
        "When": "1923",
        "Artist": "Vasily Kandinsky",
        "Medium": "Oil Painting",
        "Place": "Moscow",
        "Periods": ["Suprematism", "Abstract art"]
    },
    "Royal Red and Blue": {
        "When": "1954–1954",
        "Artist": "Mark Rothko",
        "Medium": "Oil Paint",
        "Place": "Litvak Descent",
        "Periods": ["Washington Color School"]
    },
    "Starry Night": {
        "When": "1889",
        "Artist": "Vincent van Gogh",
        "Medium": "Oil Painting",
        "Place": "Netherlands",
        "Periods": ["Post-Impressionism", "Modern art"]
    },
    # ...etc
}

@app.route("/art/<painting_name>")
#Returns information on a painting in the collection."""
def get_painting(painting_name):
    
    # If there's no such painting, we return a 404 NOT FOUND error!
    if not painting_name in art_dict:
        abort(404)
    
    return json.dumps(art_dict[painting_name])

@app.route("/artists/<artist_name>")
#Returns a list of paintings by a given artist."""
def get_artist(artist_name):
    art_list = []
    for painting in art_dict.values():
        if artist_name == painting["Artist"]: 
            art_list.append(painting)
    
    # If there's no such artist, we return a 404 NOT FOUND error!
    if not art_list:
        abort(404)

    return json.dumps(art_list)