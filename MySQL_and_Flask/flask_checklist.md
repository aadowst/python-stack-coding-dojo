## Pre-req
pipenv needs to be installed by pip
```
pip install pipenv
```
# Checklist
- create a folder for your assignment
- navigate to that folder in bash
- create virtual environment
```
    python -m pipenv 
    pipenv install flask
```
-Launch the virtual env
```
pipenv shell
```
- _Warning_ check for the files "pipefile" and "pipefile.lock"
    - If you don't see these, you need to fix it right away

************************************************************

### File structure list:

- assignment folder
     - flask_app
        - config
            - mysqlconnection.py
        - controllers
            - controller_driver.py (one for each table)
        - models 
            model_driver.py (one for each table)
    - templates
        - index.html
    - static
        -css
            - style.css
        - js
            - script.js
    - \_\_init__.py
    - pipfile
    - pipfile.lock
    - server.py
    

Example:  controller_car.py and model_car.py
*******************************
## Server.py file

```py

# Includes render requests and POST form submissions
from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

# where to import the class and what's the class name
from friend import Friend


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    return redirect('/') #Don't put render_template here!!!

@app.route('/')          
def index():
    # running the class method get_all from Friend
    friends = Friend.get_all()
    return render_template("index.html", friends=friends) 


# THIS MUST BE ON THE BOTTOM
if __name__=="__main__": 
    app.run(debug=True)   
```
***********************************************
## MySQLConnection.py

```py
# a cursor is the object we use to interact with the database
import pymysql.cursors
# this class will give us an instance of a connection to our database
class MySQLConnection:
    def __init__(self, db):
        # change the user and password as needed
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root', 
                                    password = 'root', 
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = True)
        # establish the connection to the database
        self.connection = connection
    # the method to query the database
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
     
                cursor.execute(query)
                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result
                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            except Exception as e:
                # if the query fails the method will return FALSE
                print("Something went wrong", e)
                return False
            finally:
                # close the connection
                self.connection.close() 
# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)
```

## Model_table_name.py

```py
# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('first_flask').query_db(query)
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append( cls(friend) )
        return friends
```