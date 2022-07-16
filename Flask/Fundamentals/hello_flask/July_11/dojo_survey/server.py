# Name of Assignment 
from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes



@app.route('/process', methods=['POST'])
def submit_data():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['ft_pt'] = request.form['ft_pt']
    if (request.form['comments']):
        session['comments'] = request.form['comments']
    else:
        pass
    print(request.form)
    return redirect("/result")	 
    

@app.route("/result")
def show_data():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("result.html")

@app.route('/')          
def index():
    return render_template("index.html") 


# THIS MUST BE ON THE BOTTOM
if __name__=="__main__": 
    app.run(debug=True)  