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

# we only use CRUD to help create a loop to get the entry text here
# maybe also to create a search here
# the rest of the data (weather and location) will be produced
# dynamically meaning that it has to load from front page AND THEN saved
# to the backend

entries_in_db = []
for entry in entry_data:
    # need entry_data to hold JSON strings (needs to be defined) -> Need to get Front end API data here
    # (can do this because we use JSON to tranlate the data above! JSON -- key: value)
    entry_text, date_created, weather = (Entry['entry_text'], 
                                    Entry['date_created'], 
                                    #this date_created would be automated?
                                    Entry['weather'])

    db_new_entry = crud.create_new_entry(entry_text,
                                    date_created,
                                    weather,
                                    lat,
                                    long)
    #print(db_new_movie)
    #do we need to use db, explain CRUD
    #CRUD is an idea of abstraction, we put multiple functions within DBs in CRUD so
    #file updates are easier and acessibility is easier

    entries_in_db.append(db_new_entry)


medias_in_db = []
for media in media_data:
    # need media to hold JSON strings (needs to be defined) -> Need to get Front end API data here
    # (can do this because we use JSON to tranlate the data above! JSON -- key: value)
    title, description, image_url = (Media['title'], 
                                    Media['description'], 
                                    Media['image_url'])

    db_new_media_upload = crud.create_new_media(title,
                                    description,
                                    image_url)
    #print(db_new_movie)
    #do we need to use db, explain CRUD
    #CRUD is an idea of abstraction, we put multiple functions within DBs in CRUD so
    #file updates are easier and acessibility is easier

    medias_in_db.append(db_new_media_upload)