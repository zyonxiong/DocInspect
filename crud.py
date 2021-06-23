"""CRUD Operations"""

from model import db, User, Entry, Media, connect_to_db
from datetime import datetime

def create_user(username, password):
    """Create and return a new user."""

    user = User(
        username=username,
        password=password)
        
    db.session.add(user)
    db.session.commit()

    return user


def create_new_entry(user_id, entry_text, date_created, weather, 
                    latitude, longitude):

    entry = Entry(
        user_id=user_id,
        entry_text=entry_text,
        date_created=date_created,
        weather=weather,
        latitude=latitude,
        longitutde=longitude
    )
    db.session.add(entry)
    db.session.commit()

    return entry


def check_user_login_info(username, password):
    """Return users email and password match in database"""
    
    return User.query.filter((User.username == username) & (User.password == password)).first()
    
#maybe in the future will need some user information and create information here.
#for now just create and make sure login information works

def create_new_media(title, description, image_url):

    media = Media(
        title=title,
        description=description,
        image_url=image_url
    )

    db.session.add(Media)
    db.session.commit()

    return media
    

def get_all_entries():

    """Return all the entries."""

    return Entry.query.all()




if __name__ == '__main__':
    from server import app
    connect_to_db(app)