"""CRUD Operations"""

from model import db, User, Entry, Media, connect_to_db

def create_user(username, password):
    """Create and return a new user."""

    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return user

def create_new_entry():

    db.session
    db.session
    

def create_new_media():


if __name__ == '__main__':
    from server import app
    connect_to_db(app)