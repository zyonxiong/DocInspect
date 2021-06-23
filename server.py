
from flask import (Flask, render_template, request, flash, session, redirect)
import crud

#to throw errors for jinja2 so we will see it instead of error being silent
from jinja2 import StrictUndefined

app = Flask(__name__)

@app.route('/')
def homepage():

    """Displays the app's homepage with login."""

    return render_template("Login_Page.html")


@app.route('/create-new-account', methods=["POST"])
def create_user():
    """Creates a new account, new user."""
    
    username = request.form.get("username")
    password = request.form.get("password")

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
    
    username = request.form.get('username')
    password = request.form.get('password')
    
    user = crud.check_user_login_info(username, password)
    
    if "user_id" not in session:
        session["user_id"] = user.user_id
    else:
        active_user = session.get("user_id")
        
    if user:
        flash(f"{user.email}, Successful login")
    else:
        flash("Login info is incorrect, please try again")    

    return redirect ('/')



@app.route('/main-page')
def profile():

    """Displays main entry page."""
    # this needs to be async because the page will update the entries on showing
    # and clearing forms, but does not do anything else

    return render_template('User Homepage.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

#use localhost:5000