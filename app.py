import os
from flask import Flask, jsonify
import requests
from movie_api import list_movies, list_characters

app = Flask(__name__)

port = int(os.environ['PORT'])

@app.route("/", methods=['GET'])
def index():
    return "Hello, world!"

@app.route("/movies", methods=['GET'])
def get_movies():
    movies = list_movies()
    return jsonify(movies)

@app.route("/characters/<int:movie_id>", methods=['GET'])
def get_characters(movie_id):
    characters = list_characters(movie_id)
    return jsonify(characters)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=port)
