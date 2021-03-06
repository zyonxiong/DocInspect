
from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import Entry, Media, User, connect_to_db
import crud
from app_secrets import CLOUDINARY_KEY, CLOUDINARY_SECRET, CLOUD_NAME, WEATHER_KEY
import cloudinary.uploader
import requests
import json
import os

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
    
    users = crud.get_all_usernames()

    return render_template('all_users.html', users=users)


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

@app.route('/login')
def user_login():

    """Log a user into DocInspect."""
    
    username = request.args.get('login-username')
    password = request.args.get('login-password')
    
    user = crud.check_user_login_info(username, password)
    
    if user:
        session["user_id"] = user.user_id
        # flash(f"{user.username}, Successful login")
    else:
        flash("Login info is incorrect, please try again or create a new account.")    

    print("**************")
    print(session)

    return render_template('User_Homepage.html', user=user)

@app.route('/logout')
def user_logout():

    """Log out a user from DocInspect"""
    print("Before clearing session", session)
    session.clear()
    # flash('Logged out!')
    print('After clearing session', session)
    return redirect('/')


@app.route('/add-entry', methods=["GET","POST"])
def add_entry():

    user_id = session['user_id']
    entry_text = request.form.get('entry')
    date_created = request.form.get('date')
    weather_condition = request.form.get('weather-condition')
    weather_temperature = request.form.get('weather-temperature')
    longitude = request.form.get('longitude') 
    latitude = request.form.get('latitude')
    
    new_entry = crud.create_new_entry(user_id, entry_text,
                                   date_created, weather_condition,
                                   weather_temperature, latitude, longitude)

    title = request.form.get('title')
    description = request.form.get('description')
    img_url = request.files.get('image_url')
    
    media_file = request.files['file_name']

    result = cloudinary.uploader.upload(media_file,
                                        api_key=CLOUDINARY_KEY,
                                        api_secret=CLOUDINARY_SECRET,
                                        cloud_name=CLOUD_NAME)

    img_url = result['url']

    new_media = crud.create_new_media(new_entry,title,description,img_url)

    return redirect('/view-entries')

    
@app.route('/add-entry-form')
def show_entry_form():

    """Show the entry form from User Homepage"""

    user_id = session.get('user_id')

    user = crud.get_user_info(user_id)

    return render_template('User_Homepage.html', user=user )

@app.route('/geoapi/')
def secure_geo_api_route():
    
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')

    # url = f'https://api.weatherapi.com/v1/current.json?key={WEATHER_KEY}&q={latitude},{longitude}'
    # payload = {'key': WEATHER_KEY,
    # 'q': latitude, longitude}

    res = requests.get(f'https://api.weatherapi.com/v1/current.json?key={WEATHER_KEY}&q={latitude},{longitude}')
    data = res.json()
    
    return jsonify(data)
    


@app.route('/view-entries')
def view_all_entries():
    """View a list of all the entries of a single user."""

    user_id = session.get('user_id')

    if user_id is None:

        return redirect('/')


    user_entries = crud.get_all_entries_by_user_id(user_id)

    return render_template('all_entries.html', user_entries=user_entries)


@app.route('/search-associated-entries')
def keyword_search():

    #perform a query here where the keyword is entered and database finds
    #matches that matches either one or multiple keywords
    
    return render_template('searching_for_keywords.html')


@app.route('/show-keyword-result')
def show_entries_with_keyword():

    
    user_id = session.get('user_id')

    keyword = request.args.get('search')

    user_entries = crud.find_keyword(keyword, user_id)

    return render_template('all_entries.html', user_entries=user_entries)




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

#use localhost:5000