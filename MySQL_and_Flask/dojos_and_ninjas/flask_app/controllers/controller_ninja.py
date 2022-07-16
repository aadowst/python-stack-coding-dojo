from flask_app import app
from flask import render_template, redirect, request

from flask_app.models.model_ninja import Ninja
from flask_app.models.model_dojo import Dojo


@app.route('/createninja', methods=["POST"])
def create_ninja_action():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    Ninja.save(data)
    return redirect(f'/dojo/{request.form["dojo_id"]}')


@app.route('/ninjas')
def create_ninja_display():
    dojos = Dojo.get_all()
    return render_template("create_ninja.html", dojos=dojos)







