from flask import Flask, render_template, request, redirect
# import the class from friend.py
from friend import Friend
app = Flask(__name__)
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", friends=friends)
            

@app.route('/users/<int:id>')
def show_user(id):
    # get the info about the specific user
    friend = Friend.get_one({"id":id})
    return render_template ("user.html", friend=friend)

@app.route('/submit', methods=["POST"])
def create_friend():
    data = {
        "first_name": request.form["fname"],
        "last_name" : request.form["lname"],
        "email" : request.form["email"]
    }
    id = Friend.save(data)
    url = f"/users/{id}"
    return redirect(url)

@app.route('/submit_edit', methods=["POST"])
def edit_friend():

    data = {
        "id": request.form["id"],
        "first_name": request.form["fname"],
        "last_name" : request.form["lname"],
        "email" : request.form["email"]
    }
    id = request.form["id"]
    url = f"/users/{id}"
    Friend.edit(data)

    return redirect(url)

@app.route('/users/<int:id>/destroy')
def delete_user(id):
    Friend.delete({"id":id})
    return redirect('/')

@app.route('/users/<int:id>/edit')
def edit_user(id):
    friend = Friend.get_one({"id":id})
    return render_template("edit.html", friend=friend)

@app.route('/users/new')
def new():
    return render_template("create.html")

if __name__ == "__main__":
    app.run(debug=True)