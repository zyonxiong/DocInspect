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
                    lat, long):

    entry = Entry(
        user_id=user_id,
        entry_text=entry_text,
        date_created=date_created,
        weather=weather,
        lat=lat,
        long=long
    )
    db.session.add(entry)
    db.session.commit()

    return entry
    

def create_new_media(title, description, image_url):

    media = Media(
        title=title,
        description=description,
        image_url=image_url
    )

    db.session.add(Media)
    db.session.commit()




if __name__ == '__main__':
    from server import app
    connect_to_db(app)