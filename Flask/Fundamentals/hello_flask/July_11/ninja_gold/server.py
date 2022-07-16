# Ninja Gold
from flask import Flask, render_template, request, redirect, session
import random


app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes


@app.route('/process_money', methods=['POST'])
def increase_count():
    print(request.form['choice'])
    print("please print")
    guesses_left = int(session['count'])-1
    session['count']= guesses_left
    choice = request.form['choice']
    message = "this is a message"
    if(choice == "Farm"):
        last_gold = random.randint(10,20)
        session['total_gold'] = int(session['total_gold']) + last_gold
    elif(choice =="Cave"):
        last_gold = random.randint(5,10)
        session['total_gold'] = int(session['total_gold']) + last_gold
    elif(choice =="House"):
        last_gold = random.randint(2,5)
        session['total_gold'] = int(session['total_gold']) + last_gold
    else:
        last_gold = random.randint(-50,50)
        session['total_gold'] = int(session['total_gold']) + last_gold

    if(last_gold < 0):
        win_loss = "lost"
        last_gold = abs(last_gold)
        span = "<span id='lost'>"
    else:
        win_loss = "won"
        span = "<span id='won'>"

    message = f"{span}You just {win_loss} {last_gold} gold at the {choice} </span><br>" + session['activities']
    session['activities'] = message


    return redirect("/")	




@app.route('/')          
def index():
    if("count" in session and "activities" in session):
        pass
    else:
        session['count'] = 15
        session['total_gold'] = 0
        session['last_gold'] = ""
        session['activities'] = ""


    return render_template("index.html") 


# THIS MUST BE ON THE BOTTOM
if __name__=="__main__": 
    app.run(debug=True)  