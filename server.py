
from flask import (Flask, render_template, request, flash, session, redirect)

#to throw errors for jinja2 so we will see it instead of error being silent
from jinja2 import StrictUndefined

app = Flask(__name__)

@app.route('/')
def homepage():

    # """Displays the app's homepage."""
    
    # email = request.form.get("email")
    # password = request.form.get("password")

    # user = crud.get_user_by_email(email)
    # if user:
    #     flash("Cannot create an account with that email. Try again.")
    # else:
    #     crud.create_user(email, password)
    #     flash("Account created! Please log in.")

    # return redirect("/")


    return render_template("Login_Page.html")


@app.route('/create-new-account')
def create():
    """Creates a new account."""

    return render_template("Create_New_Account.html")

@app.route('/main-page')
def profile():

    """Displays main entry page."""

    return render_template('User Homepage.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

#use localhost:5000