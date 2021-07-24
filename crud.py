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


def get_user_by_username(username):
    """Return a user by username."""

    return User.query.filter(User.username == username).first()


def check_user_login_info(username, password):
    """Return username and password match in database"""
    
    return User.query.filter((User.username == username) & (User.password == password)).first()

def get_all_usernames():
    """Return all usernames"""

    return User.query.all()


def get_user_info(user_id):
    """Get the User's detail"""

    return User.query.get(user_id)

#maybe in the future will need some user information and create information here.
#for now just create and make sure login information works

def create_new_entry(user_id, entry_text, date_created, weather, 
                    latitude, longitude):

    entry = Entry(
        user_id=user_id,
        entry_text=entry_text,
        date_created=date_created,
        weather=weather,
        latitude=latitude,
        longitude=longitude
    )
    db.session.add(entry)
    db.session.commit()

    return entry

def get_entry_by_id(entry_id):
    """Return entry by id"""

    return Entry.query.get(entry_id)
    
def get_all_entries_by_user_id(user_id):

    return Entry.query.filter_by(user_id = user_id).all()


def get_all_entries():

    """Return all the entries."""

    return Entry.query.all()


def create_new_media(entry, title, description, image_url):

    media = Media(
        media_entry = entry,
        title=title,
        description=description,
        image_url=image_url
    )

    db.session.add(media)
    db.session.commit()

    return media


def get_all_medias():

    """Return all media"""

    return Media.query.all()



if __name__ == '__main__':
    from server import app
    connect_to_db(app)