# from traitlets import Int
from datetime import datetime
from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

# this works. coded {{fruit_sum}} in the html
# @app.route('/checkout', methods=['POST'])         
# def checkout():
#     print(request.form)
#     form_data = request.form
#     fruit_sum = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
#     return render_template("checkout.html", form_data = form_data, fruit_sum = fruit_sum)

# this also works. typecast the numbers of each fruit and added them together in jinja2 as shown below:
# {{ request.form['strawberry']|int + request.form['raspberry']|int + request.form['apple']|int }}
@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    dt = datetime.now()
    str_date = dt.strftime("%d %b, %Y at %H:%M")
    form_data = request.form
    return render_template("checkout.html", form_data = form_data, str_date = str_date)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    