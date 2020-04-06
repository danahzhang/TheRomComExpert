#Import Dependency
import numpy as np

import os

from flask import Flask, jsonify, render_template, make_response, abort

#Import Files
print("Warning!!!\n")
print("You should run the short version because the long version will take hours!!!")
question = input("Long(l) or Short(s): ")
if question.lower() =="l":
    print("You picked the short option.")
    import json_create_long
    from json_create import movie_dictionary
elif question.lower() == "s":
    print("You picked the short option.")
    import json_create
    from json_create import movie_dictionary
else:
    print("You picked the short option by default.")
    import json_create
    from json_create import movie_dictionary
import sqlite_create
import list_create

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
app._static_folder = os.path.abspath("templates/static/")

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """Return Home"""
    return render_template('home.html')

@app.route("/home.html")
def welcomeback():
    """Return Home"""
    return render_template('home.html')

@app.route("/data.html")
def data():
    """Data Page"""
    return render_template('data.html')


@app.route("/graphs.html")
def graphs():
    """Graph Page"""
    return render_template('graphs.html')

@app.route("/data/id/<imdbid>",methods=['GET'])
def apiinfo(imdbid):
    iding = [movie for movie in movie_dictionary['movies'] if movie['imdbID'] == imdbid]
    if len(id) == 0:
        abort(404)
    return jsonify({'movies': iding[0]})

@app.route("/data/title/<title>",methods=['GET'])
def filmtitle(title):
    moviename = [movie for movie in movie_dictionary['movies'] if movie['Title'].lower().replace(" ","") == title.lower().replace(" ","")]
    if len(moviename) == 0:
        abort(404)
    return jsonify({'movies': moviename})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run(debug=True)
