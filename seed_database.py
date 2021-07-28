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

entries_in_db = []

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
weather_temps = ['70, 80, 60']

for i in range(10):
    entry_text = fake.texts()
    date_created = fake.date_time()
    weather_condition = random.choice(weather_conditions)
    weather_temperature = random.choice(weather_temps)
    latitude = fake.latitude()
    longitude = fake.longitude()
    user = random.choice(users)
    entry = crud.create_new_entry(user.user_id, entry_text, date_created,
                                weather_condition, weather_temperature,
                                latitude, longitude)
    entries.append(entry)

        
#create 10 fake entries

medias = []

for i in range(10):
    title = fake.file_name().split('.')[0]
    description = fake.sentence()
    image_url = fake.image_url()
    entry = random.choice(entries)
    media = crud.create_new_media(entry, title, description, image_url)
    medias.append(media)

#create 10 fake images