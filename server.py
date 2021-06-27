
from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud
import os
import cloudinary.uploader

#to throw errors for jinja2 so we will see it instead of error being silent
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'secretmessage'


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

    return render_template('/User Homepage.html')



@app.route('/main-page')
def profile():

    """Displays main entry page."""
    # this needs to be async because the page will update the entries on showing
    # and clearing forms, but does not do anything else

    return render_template('User Homepage.html')


@app.route('/add-entry', methods=["POST"])
def add_entry():

    entry_text = request.form.get("entry")
    date_created = request.form.get("date")
    weather = request.form.get('weather')
    location = request.form.get('longitude', 'latitude')
    media = request.files['media']
    media = cloudinary.uploader.upload(media,
                                        api_key=CLOUDINARY_KEY,
                                        api_secret=CLOUDINARY_KEY_SECRET,
                                        could_name=zxiong)






if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

#use localhost:5000