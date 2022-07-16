# Name of Assignment 
from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)  

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes


# @app.route('/guess', methods=['POST'])
# def increase_count():
#     guesses_left = int(session['count'])-1
#     session['count']= guesses_left
#     session['guess'] = request.form['guess']

#     if(int(session['guess']) == int(session['number'])):
#         return redirect("/winner")
#     elif (int(session['guess']) > int(session['number'])):
#         high_low = "High"
#     else:
#         high_low = "Low"
#     return high_low, redirect("/wrong")

@app.route('/guess', methods=['POST'])
def increase_count():
    guesses_left = int(session['count'])-1
    session['count']= guesses_left
    session['guess'] = request.form['guess']

    if(session['guess'] == session['number']):
        return redirect("/winner")

    elif (int(session['guess']) > int(session['number']) and guesses_left >0):
        session['high_low'] = "High"
        return redirect("/wrong")

    elif (int(session['guess']) < int(session['number']) and guesses_left >0):
        session['high_low'] = "Low"
        return redirect("/wrong")
    else:
        return redirect("/loser")

@app.route("/loser")
def loser():
    return render_template("loser.html")

@app.route("/wrong")
def wrong():
    return render_template("wrong.html")

@app.route("/winner")
def winner():
    return render_template("winner.html")

@app.route('/play_again', methods=['POST'])
def reset_counter():
    session.pop('number')
    session.pop('guess')
    session.pop('high_low')
    session['count']= 5
    return redirect("/")	

@app.route('/')          
def index():
    if 'number' in session:
        pass
    else:
        session['number'] = random.randint(1,100)
    return render_template("index.html") 


# THIS MUST BE ON THE BOTTOM
if __name__=="__main__": 
    app.run(debug=True)  