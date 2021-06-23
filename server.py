
from flask import (Flask, render_template, request, flash, session, redirect)
import crud

#to throw errors for jinja2 so we will see it instead of error being silent
from jinja2 import StrictUndefined

app = Flask(__name__)

@app.route('/')
def homepage():

    """Displays the app's homepage."""
    
    username = request.form.get("username")
    password = request.form.get("password")

    user = crud.get_user_by_username(username)
    if user:
         flash("Cannot create an account with that email. Try again.")
    else:
        crud.create_user(username, password)
        flash("Account created! Please log in.")

    # return redirect("/")


    return render_template("Login_Page.html")


@app.route('/create-new-account')
def create():
    """Creates a new account."""

    return render_template("Create_New_Account.html")

@app.route('/main-page')
def profile():

    """Displays main entry page."""
    # this needs to be async because the page will update the entries on showing
    # and clearing forms, but does not do anything else

    return render_template('User Homepage.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

#use localhost:5000