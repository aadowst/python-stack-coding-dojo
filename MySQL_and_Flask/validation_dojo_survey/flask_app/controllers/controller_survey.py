from flask_app import app
from flask import render_template, redirect, request

from flask_app.models.model_survey import Survey


# Create Action 
@app.route('/process', methods=["POST"])
def submit_survey():
    if not Survey.validate_comment(request.form):
        return redirect ('/')
    id = Survey.save(request.form)
    url = f"/comment/{id}"
    return redirect(url)

# Create Display NOT NEEDED
# @app.route('/users/new')
# def new():
#     return render_template("create.html")

# Read 
@app.route('/')
def index():
    # call the get all classmethod to get all ninjas

    return render_template("index.html")
            

@app.route('/comment/<int:id>')
def read_one_commment(id):
    comment = Survey.get_one({"id": id})
    print(comment)
    return render_template("result.html", comment=comment)
    


# ***********************************UPDATE TO GO HERE ******************************************

# ************************************DELETE TO GO HERE*****************************************

