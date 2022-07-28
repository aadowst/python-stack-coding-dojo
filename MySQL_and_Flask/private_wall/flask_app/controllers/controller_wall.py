

from flask_app import app
from flask import render_template, redirect, request, session, flash


from flask_app.models import model_wall, model_user





# Create Display NOT NEEDED
# @app.route('/users/new')
# def new():
#     return render_template("create.html")

# Read 




@app.route('/wall')
def wall():
    if 'user_id' not in session:
        return redirect('/')
    other_users = model_user.User.get_all_not_user({"id": session['user_id']})

    users_messages = model_wall.Wall.get_all_user_messages({"recipient_id": session['user_id']})
    message_count = model_wall.Wall.count_messages({"sender_id": session['user_id']})
    print("message count is:  ",message_count)

    return render_template("wall.html", other_users=other_users, users_messages = users_messages, message_count = message_count)

# could/should this route be messages/send? we have user id in session (and/or could create the context variable that Tyler showed)
@app.route('/messages/<int:recipient_id>/send', methods=["post"])
def add_one(recipient_id):

    # if not Model.validate_input(request.form):
    #     return redirect ('/')

    data = {
        **request.form,
        "recipient_id": recipient_id,
        "sender_id": session["user_id"]
    }

    model_wall.Wall.create_message(data)

    return redirect("/wall")


@app.route('/messages/<int:id>/delete')
def delete_one(id):
    model_wall.Wall.delete({"id": id})
    return redirect("/wall")

# @app.route('/delete', methods=["POST"])
# def delete_email():
#     id = request.form["id"]
#     print("id is:  ", id)
#     print("request.form id is: ", request.form["id"])
#     User.delete(request.form)
#     return redirect('/')
    

