from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/success')
def success():
	return "success"

@app.route('/hello/<name>/<id>')
def hello(name, id):
	# print(name)
	# print(id)
	return "hello, " + name + ". Your Member Number is " + id

if __name__=="__main__":
	app.run(debug=True)
