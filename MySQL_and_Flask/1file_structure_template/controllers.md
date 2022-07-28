```py

from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash

from flask_app.models.model_name import Modelname

@app.route('/')
def index():
    if 'user_id' not in session:
        return render_template("index.html")
    return redirect('/dashboard')

# *************************CREATE*******************************

# ADD TO DB ACTION
@app.route('/submit', methods=["POST"])
def add_one():

    if not Model.validate_input(request.form):
        return redirect ('/')

    id = Model.save(request.form)
    return redirect(f"/model/{id}")

# if the above doesn't work try:

@app.route('/createone', methods=["POST"])
def create_one_action():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    Model.save(data)
    return redirect(f'/entry/{request.form["entry_id"]}')


# DISPLAY
@app.route('/entry/create')
def new_entry():
    return render_template("entry_create.html")

# ********************************READ*******************************************



# READ ONE
@app.route('/success/<int:id>')
def read_one_commment(id):
    one_data = Modelname.get_one({"id": id})
    all_data = Modelname.get_all()
    return render_template("result.html", one_data = one_data, all_data=all_data)

# READ ALL

@app.route("/model")
def index():

    all_data = Model.get_all()
    print(all_data)
    return render_template("index.html", all_data=all_data)

# ********************************UPDATE*****************************************

# ACTION
@app.route('/submit_edit', methods=["POST"])
def edit_one_action():
    Friend.edit(request.form)

    id = request.form["id"]
    url = f"/users/{id}"
    return redirect(url)
    
# DISPLAY
@app.route('/entry/<int:id>/edit')
def edit_one_display(id):
    one_data = Model.get_one({"id":id})
    return render_template("edit.html", one_data=one_data)

# *********************************DELETE*******************************************

# USING POST DATA
@app.route('/delete', methods=["POST"])
def delete_one():
    # id = request.form["id"]
    # print("id is:  ", id)
    # print("request.form id is: ", request.form["id"])
    Model.delete(request.form)
    return redirect('/')

# USING GET DATA
@app.route('/entry/<int:id>/delete')
def delete_one(id):
    Model.delete({"id":id})
    return redirect('/')

# <!-- ************************LOGIN AND REGISTRATION************************************************ -->

# LOGIN
    if not user_in_db:
        flash("invalid email or password", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("invalid email or password", "login")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')


# DASHBOARD

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return render_template("dashboard.html")
    return redirect('/')


# LOG OUT
@app.route('/logout')
def logout():
    del session["user_id"]
    return redirect ('/')

# Alternate approach to log out
@app.route('/logout')
def logout():
    session.clear()
    return redirect ('/')


# REGISTER
@app.route('/register', methods=["POST"])
def register():

    if not User.validate_registration(request.form):
        return redirect ('/')

    password_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password': password_hash
    }

    user_id = User.save(data)
    session['user_id'] = user_id
    return redirect('/dashboard')

```
