# Name of Assignment 
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes



@app.route('/count', methods=['POST'])
def increase_count():
    increased_count = int(session['count'])+1
    session['count']= increased_count
    return redirect("/")	 

@app.route('/specify_increment', methods=['POST'])
def specify_count():
    specified_count = int(session['count']) + int(request.form['increment']) - 1
    session['count']= specified_count
    return redirect("/")

@app.route('/destroy_session', methods=['POST'])

def reset_counter():
    session['count']= 0
    return redirect("/")	

@app.route('/')          
def index():
    increased_count = int(session['count'])+1
    session['count']= increased_count
    return render_template("index.html") 


# THIS MUST BE ON THE BOTTOM
if __name__=="__main__": 
    app.run(debug=True)  