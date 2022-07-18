
from flask_app import app
from flask import render_template, redirect, request

from flask_app.models.model_email import Email


# Create Action 
@app.route('/process', methods=["POST"])
def submit_email():
    if not Email.validate_email(request.form):
        return redirect ('/')
    id = Email.save(request.form)
    print(id)
    return redirect(f'/success/{id}')


# Create Display NOT NEEDED
# @app.route('/users/new')
# def new():
#     return render_template("create.html")

# Read 
@app.route('/')
def index():
    return render_template("index.html")
            

@app.route('/success/<int:id>')
def read_one_commment(id):
    email = Email.get_one({"id": id})
    all_emails = Email.get_all()
    return render_template("result.html", email=email, all_emails=all_emails)

@app.route('/delete', methods=["POST"])
def delete_email():
    id = request.form["id"]
    print("id is:  ", id)
    print("request.form id is: ", request.form["id"])
    Email.delete(request.form)
    return redirect('/')
    


# ***********************************UPDATE TO GO HERE ******************************************

# ************************************DELETE TO GO HERE*****************************************

