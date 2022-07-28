
from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.models.model_user import User, Friendship

@app.route('/friendships')
def index():
    all_users = User.get_all_users()
    all_friendships = "deleteme"
    all_friendships = User.get_all_friendships()
    print(all_users)
    return render_template("index.html", all_users=all_users, all_friendships=all_friendships)

@app.route('/adduser', methods=["post"])
def add_user():
    User.save_user(request.form)
    return redirect('/friendships')



@app.route('/createfriendship', methods=["post"])
def create_friendship():
    
    return redirect('/friendships')