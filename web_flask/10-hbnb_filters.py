#!/usr/bin/python3
"""Starts a Flask web application with filters for AirBnB_clone_v2"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Displays a HTML page with filters"""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda amenity: amenity.name)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

