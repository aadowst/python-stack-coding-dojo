# Playground
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
	return render_template("index.html", phrase ="hello", times=5)

@app.route('/success')
def success():
	return "success"

# *******LEVEL 1*********
# @app.route('/play')
# def play():
# 	return render_template("play.html")

# *********LEVEL 2*********
# @app.route('/play/<int:count>')
# def play(count):
# 	return render_template("play.html", count=count)

# ********LEVEL 3***********
@app.route('/play/<int:count>/<string:color>')
def play(count, color):
	return render_template("play.html", count=count, color=color)


if __name__=="__main__":
	app.run(debug=True)