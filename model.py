from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

#Creates an instance
db = SQLAlchemy()

class User(db.Model):

    """A User database."""

    __tablename__= "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)

    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))

    entries = db.relationship('Entry', back_populates='user')

    def __repr__(self):
         return f'<User user_id={self.user_id} username={self.username}>'



class Entry(db.Model):

    """A entry database."""

    __tablename__= "entries"

    entry_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)

    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        nullable=False)

    entry_text = db.Column(db.String,
                        nullable=True)

    date_created = db.Column(db.DateTime,
                    nullable=True)

    weather = db.Column(db.String(50),
                        nullable=True)

    latitude = db.Column(db.String(50),
                    nullable=True)

    longitude = db.Column(db.String(50),
                    nullable=True)

    medias = db.relationship('Media', back_populates = 'media_entry')
    user = db.relationship('User', back_populates = 'entries')

    def __repr__(self):
         return f'<Entry entry_id={self.entry_id} entry_text={self.entry_text} date_created={self.date_created} weather={self.weather} latitude={self.latitude} longitude={self.longitude}>'



class Media(db.Model):

    """A media database."""

    __tablename__= "medias"

    media_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)

    title = db.Column(db.String(50),
                      nullable=False,
                      unique = True)

    description = db.Column(db.String(50),
                      nullable=False,
                      unique = True)
    
    image_url = db.Column(db.String(200),
                        nullable=True,
                        unique = True)

    entry_id = db.Column(db.Integer,
                        db.ForeignKey('entries.entry_id'),
                        nullable=False,)

    media_entry = db.relationship('Entry', back_populates = 'medias')

    def __repr__(self):
         return f'<Media media_id={self.media_id} title={self.title} description={self.description} image_url={self.image_url}>'
    


def connect_to_db(flask_app, db_uri='postgresql:///docentries', echo=True):
    
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':

    from server import app 
    connect_to_db(app)
