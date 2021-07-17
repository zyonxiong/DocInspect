
from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import Entry, connect_to_db
import crud
from app_secrets import CLOUDINARY_KEY, CLOUDINARY_SECRET, WEATHER_KEY, GOOGLE_KEY
import cloudinary.uploader
import requests
import json

#to throw errors for jinja2 so we will see it instead of error being silent
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'secretmessage'

#refer by variable for key name


@app.route('/')
def homepage():

    """Displays the app's homepage with login."""

    return render_template("Login_Page.html")


@app.route('/users')
def list_of_users():
    """Gives a list of users."""
    
    user = crud.get_all_usernames()

    return render_template('/all_users.html', user=user)


@app.route('/users', methods=['POST'])
def register_user():
    """Create a new user"""
    
    username = request.form.get('username')
    password = request.form.get('password')
    
    user = crud.get_user_by_username(username)
    
    if user:
        flash("Username already exist. Please try a new username.")
    else:
        crud.create_user(username, password)
        flash("Account created! Please log in.")

    return redirect("/")

@app.route('/login', methods=['POST'])
def user_login():

    """Log a user into DocInspect."""
    
    username = request.form.get('username')
    password = request.form.get('password')
    
    user = crud.check_user_login_info(username, password)
    
    if "user_id" not in session:
        session["user_id"] = user.user_id
    else:
        active_user = session.get("user_id")
        
    if user:
        flash(f"{user.username}, Successful login")
    else:
        flash("Login info is incorrect, please try again")    

    return render_template('User_Homepage.html')


@app.route('/add-entry', methods=["GET","POST"])
def add_entry():

    user_id = session['user_id']
    entry_text = request.form.get('entry')
    date_created = request.form.get('date')
    weather = request.form.get('weather')
    longitude = request.form.get('longitude') #this to grab from API
    latitude = request.form.get('latitude') #this to grab from API

    url = 'https://api.weatherapi.com/v1/current.json'
    payload = {'key': WEATHER_KEY,
    'latitude': latitude,
    'longitude': longitude,
    'weather': weather}

    res = requests.get(url, params=payload)
    #res.json()
    # if res is correct, then pass
    # else if res is incorrect, then message should state that 
    # request cannot be made 
    
    # new_entry = crud.create_new_entry(user_id, entry_text,
    #                                 date_created, weather, 
    #                                   latitude, longitude)

    return redirect('/view-entries')

@app.route('/view-entries')
def view_all_entries():
    """View a list of all the entries of a single user."""

    user_id = session.get('user_id')

    if user_id is None:

        return redirect('/')

    user_entries = crud.get_all_entries_by_user_id(user_id)

    return render_template('all_entries.html', user_entries=user_entries)


#media here


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

#use localhost:5000