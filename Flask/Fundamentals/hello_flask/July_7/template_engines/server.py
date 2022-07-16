from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
	return render_template("index.html", phrase ="hello", times=5)

@app.route('/success')
def success():
	return "success"

@app.route('/hello/<string:name>/<int:id>')
def hello(name, id):
	return render_template("hello.html", name=name, id=id)


if __name__=="__main__":
	app.run(debug=True)