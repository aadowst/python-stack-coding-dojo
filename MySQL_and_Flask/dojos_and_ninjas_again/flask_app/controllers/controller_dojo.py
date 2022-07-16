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
    dojo = Dojo.get_dojo_with_ninjas({"id": id})
    print(dojo)
    return render_template("one_dojo.html", dojo=dojo)
    


# ***********************************UPDATE TO GO HERE ******************************************

# ************************************DELETE TO GO HERE*****************************************

