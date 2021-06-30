
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

    return render_template('/User_Homepage.html')



@app.route('/main-page')
def profile():

    """Displays main entry page."""
    # this needs to be async because the page will update the entries on showing
    # and clearing forms, but does not do anything else

    return render_template('User_Homepage.html')


@app.route('/add-entry', methods=["POST"])
def add_entry():

    entry_text = request.form.get("entry")
    date_created = request.form.get("date")
    weather = request.form.get('weather')
    location = request.form.get('longitude', 'latitude')
    media = request.form.get('weather')
    
# weather -> comes from API
# location -> global object through all browsers -> navigator.geolocation()
# JSON format string -> convert it to a structure (.JSON)

    added_entries = crud.create_new_entry()

    return render_template('User_Homepage.html', entry_text=entry_text,
                                                date_created=date_created,
                                                weather=weather,
                                                location=location,
                                                media=media)
    #this needs to be render as a new html that will update all entries?


@app.route('/view-entries')
def view_all_entries():
    """View a list of all the entries of a single user."""

    entries = crud.get_entry_by_id(entry_id)

    return render_template('all_entries.html', entries=entries )


#need another route to display all entries associated with
#media here



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

#use localhost:5000