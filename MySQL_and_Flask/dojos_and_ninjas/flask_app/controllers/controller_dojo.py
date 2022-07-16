from flask_app import app
from flask import render_template, redirect, request

from flask_app.models.model_dojo import Dojo
from flask_app.models.model_ninja import Ninja

# Create Action 
@app.route('/createdojo', methods=["POST"])
def create_dojo_action():
    data = {
        "name": request.form["name"],
    }
    id = Dojo.save(data)
    print(id)
    url = f"/dojo/{id}"
    return redirect(url)

# Create Display NOT NEEDED
# @app.route('/users/new')
# def new():
#     return render_template("create.html")

# Read 
@app.route('/')
@app.route("/dojos")
def read_all_dojos():
    # call the get all classmethod to get all ninjas
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("index.html", dojos=dojos)
            

@app.route('/dojo/<int:id>')
def read_one_dojo(id):
    # get the info about the specific dojo
    dojo = Dojo.get_one({"id": id})
    print(dojo)
    ninjas = Ninja.ninjas_at_one_dojo({"dojo_id": id})
    return render_template ("one_dojo.html", ninjas=ninjas, dojo=dojo)

# ***********************************UPDATE TO GO HERE ******************************************

# ************************************DELETE TO GO HERE*****************************************

