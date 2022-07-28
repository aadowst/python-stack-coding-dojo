# checkerboard
from ast import Num
from flask import Flask, render_template
app = Flask(__name__)
# original code (with hardcoded checkboard pattern)
# @app.route('/')
# def index():
# 	return render_template("index.html")

@app.route('/')
def count_default(count=8, column=8):
	count = round(count/2)
	column = round(column/2)
	return render_template("index.html", count=count, column=column)

@app.route('/<int:count>')
def row_count(count, column=8):
	count = round(count/2)
	column = round(column/2)
	print(count)
	return render_template("index.html", count=count, column=column)

@app.route('/<int:count>/<int:column>')
def row_column_count(count, column):
	column = round(column/2)
	count = round(count/2)
	print(count)
	return render_template("index.html", count=count, column=column)

@app.route('/<int:count>/<int:column>/<dark>')
def row_column_count_colors(count, column, dark="green", light="peachfuzz"):
	column = round(column/2)
	count = round(count/2)
	print(count)
	return render_template("index.html", dark = dark, light = light, count = count, column = column)

@app.route('/<int:count>/<int:column>/<dark>/<light>')
def row_column_count_both_colors(count, column, dark="green", light="white"):
	column = round(column/2)
	count = round(count/2)
	print(count)
	return render_template("index.html", dark = dark, light = light, count = count, column = column)

# ********COPIED FROM PLAYGROUND***********
# @app.route('/play/<int:count>/<string:color>')
# def play(count, color):
# 	return render_template("play.html", count=count, color=color)


if __name__=="__main__":
	app.run(debug=True)