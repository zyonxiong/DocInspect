"""Script to seed database."""
# This is a module from Python’s standard library. It contains
# code related to working with your computer’s operating system.
import os

# Remember this module from the APIs lab?
# You’ll need this to load the data from the google & cloudinary API
import json

from faker import Faker
# Faker to get fake information


# We’ll use datetime.strptime to turn a string into a Python datetime object
# for time purposes in database
from datetime import datetime

# Files that are included: crud.py, model.py, and server.py.
import crud
import model
import server

os.system('dropdb docentries')
os.system('createdb docentries')

model.connect_to_db(server.app)
model.db.create_all()

# loads data from API (JSON) and saves it to a variable
# these JSON string is coming from google, weather and cloudinary

# we only use CRUD to help create a loop to get the entry text here
# maybe also to create a search here
# the rest of the data (weather and location) will be produced
# dynamically meaning that it has to load from front page AND THEN saved
# to the backend

#can only do this if everything was JSON format, but it's not. The
#only JSON format is the longitude and latitude, with the weather. So do
#I need to even set it up like this? I feel that I can just append without
#using a loop.

entries_in_db = []
# for entry in crud.Entry:
    #comment out because probably won't need this section down here
    # need entry_data to hold JSON strings (needs to be defined) -> Need to get Front end API data here
    # (can do this because we use JSON to tranlate the data above! JSON -- key: value)
    # entry_text, date_created, weather = (Entry['entry_text'], 
    #                                 Entry['date_created'], 
    #                                 #this date_created would be automated?
    #                                 Entry['weather'])

fake = Faker()
users = []

for i in range(10):
    name = fake.user_name()
    password = fake.password()
    user = crud.create_user(name, password)
    users.append(user)

#creating 10 fake users

import random

entries = []

weather_conditions = ['sunny','cloudy', 'rainy']

for i in range(10):
    entry_text = fake.texts()
    date_created = fake.date_time()
    weather = random.choice(weather_conditions)
    latitude = fake.latitutde()
    longitude = fake.longitude()
    entry = crud.create_new_entry(entry_text, date_created, weather, latitude, longitude)
    entries.append(entry)

        
#create 10 fake entries

# db_new_entry = crud.create_new_entry(entry_text, date_created, weather, latitude,
#                                     longitude)
#     do we need to use db, explain CRUD
#     CRUD is an idea of abstraction, we put multiple functions within DBs in CRUD so
#     file updates are easier and acessibility is easier

# entries_in_db.append(db_new_entry)

medias = []

for i in range(10):
    title = fake.title()
    description = fake.description()
    image_url = fake.image_url()
    media = crud.create_new_media(title, description, image_url)
    medias.append(media)


# medias_in_db = []
# for media in media_data:
#     # need media to hold JSON strings (needs to be defined) -> Need to get Front end API data here
#     # (can do this because we use JSON to tranlate the data above! JSON -- key: value)
#     title, description, image_url = (Media['title'], 
#                                     Media['description'], 
#                                     Media['image_url'])

#     db_new_media_upload = crud.create_new_media(title,
#                                     description,
#                                     image_url)
#     #do we need to use db, explain CRUD
#     #CRUD is an idea of abstraction, we put multiple functions within DBs in CRUD so
#     #file updates are easier and acessibility is easier

#     medias_in_db.append(db_new_media_upload)