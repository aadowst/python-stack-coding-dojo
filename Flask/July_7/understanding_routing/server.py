from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
	return 'Understanding Routing'

@app.route('/dojo')
def hello_dojo():
	return 'Dojo!'

@app.route('/say/<string:repeat_me>')
def repeat_me(repeat_me):
	return 'Hi, ' + repeat_me

@app.route('/<int:how_many>/<string:phrase>')
def said_it(how_many, phrase):
	said_it = phrase*how_many
	return f"You wanted me to say {said_it}"

if __name__=="__main__":
	app.run(debug=True)
