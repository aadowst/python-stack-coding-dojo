
from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash





# Read 
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/logout', methods=["get", 'POST'])
def logout():
    del session["user_id"]
    del session["first_name"]
    return redirect ('/')




