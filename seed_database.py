"""Script to seed database."""
# This is a module from Python’s standard library. It contains
# code related to working with your computer’s operating system.
import os

# Remember this module from the APIs lab?
# You’ll need this to load the data from the google & cloudinary API
import json


# We’ll use datetime.strptime to turn a string into a Python datetime object
# for time purposes in database
from datetime import datetime

# Files that are included: crud.py, model.py, and server.py.
import crud
import model
import server

os.system('dropdb docinspect')
os.system('createdb docinspect')

model.connect_to_db(server.app)
model.db.create_all()

# loads data from API (JSON) and saves it to a variable
with open('filename') as f:
    # google_geolocation_api= json.loads(f.read())