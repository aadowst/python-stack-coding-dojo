```py


import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
NAME_REGEX = re.compile(r'^[a-zA-Z\s0-9_-]{3,15}$')
# note:  name can have spaces; added \s to allow this
PASSWORD_REGEX = re.compile(r'^[a-zA-Z0-9.+_-](?=.*?[0-9]).{8,}$')

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

DATABASE = "name_of_schema"

class Model:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# #########################################################CLASS METHODS######################################################################3

# **********************************************************CREATE**********************************************************

    @classmethod
    def save_model(cls, data ):

        query = "INSERT INTO table_name ( name, location, language, comment ) VALUES ( %(name)s, %(location)s, %(language)s, %(comment)s );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(DATABASE).query_db( query, data )


# **********************************************************READ**************************************************************

# READ ALL

    @classmethod
    def get_all_models(cls):
        query = "SELECT * FROM table_name;"

        results = connectToMySQL(DATABASE).query_db(query)
        list = []
        for entry in results:
            list.append( cls(entry) )
        return list
    

# READ ONE

    @classmethod
    def get_one_model(cls, id):
        query = "SELECT * FROM table_name WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, id)
        return cls(results[0])

# READ ALL AT ONE
    @classmethod
    def get_one_with_all(cls, data):
        query = "SELECT * from one_table LEFT JOIN all_table on all_table.one_table_id = one_table.id WHERE all_table.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        one_data = cls(results[0])

        for row_from_db in results:
            all_data = {
                "id": row_from_db["all_table.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "age": row_from_db["age"],
                "one_table_id": row_from_db["id"]
            }

        one_data.all.append(model_all.Modelall(all_data))
        return one_data

# EXAMPLE OF GET_ONE_WITH_ALL
    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * from dojos LEFT JOIN ninjas on ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        dojo = cls(results[0])

        for row_from_db in results:
            ninja_data = {
                "id": row_from_db["ninjas.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "age": row_from_db["age"],
                "dojo_id": row_from_db["id"]
            }

        dojo.ninjas.append(model_ninja.Ninja(ninja_data))
        return dojo


# EXAMPLE OF GET ALL EXCEPT....
    @classmethod
    def get_all_not_favorited_by(cls, id):
        query = "select * from authors where authors.id not in (select favorites.author_id from favorites where book_id = %(id)s);"
        results = connectToMySQL('books_sql_db').query_db(query, id)
        author_list = []
        for row_from_db in results:
            author_data = {
                "id": row_from_db["id"],
                "name": row_from_db["name"],
                "created_at": row_from_db["created_at"],
                "updated_at": row_from_db["updated_at"]
            }
            author_list.append(Author(author_data))
        
        return author_list

# **********************************************UPDATE*********************************************

    @classmethod
    def edit_one_action(cls, data):
        query = "UPDATE table_name SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db( query, data)

# **************************************************DELETE*********************************************
    @classmethod
    def delete_model(cls, id):
        query = "DELETE FROM table_name WHERE id = %(id)s;"
        connectToMySQL(DATABASE).query_db(query, id)
        return



# ####################################################STATIC METHODS##########################################

# VALIDIATE INPUT

    @staticmethod
    def validate_input(post_data):
        is_valid = True

        if (len(post_data['name']) <3):
            flash("Name must be at least 3 characters")
            is_valid = False
        if " " not in post_data['name']:
            flash("Include your full name")
            is_valid = False
        if (len(post_data['location'])<3):
            flash("Location must be at least  3 characters")
            is_valid = False
        if (len(post_data['language'])<3):
            flash("Language must be at least 3 characters")
            is_valid = False
        if (len(post_data['comment'])<3):
            flash("Comments must be at least 3 characters")
            is_valid = False
        return is_valid

# EMAIL IN DB?  Note:  this was a class method before and worked there. don't know why it wouldn't work as a static method
    @staticmethod
    def email_match(data):

        query = "SELECT * FROM table_name WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)

        if not result:
            return False
        return cls(result[0])

# VALIDATE REGISTRATION

    @staticmethod
    def validate_registration(data):

        is_valid = True
        if (len(data['first_name'])<3):
            flash("please enter at least two characters in first name", "registration")
            is_valid = False
        if not NAME_REGEX.match(data['first_name']):
            flash("only alphanumeric characters are allowed in first name", "registration")
            is_valid = False


        if (len(data['last_name'])<3):
            flash("please enter at least two characters in last name", "registration")
            is_valid = False
        if not NAME_REGEX.match(data['last_name']):
            flash("only alphanumeric characters are allowed in last name", "registration")
            is_valid = False


        if (len(data['email'])<1):
            flash("please enter an email address", "registration")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Email is not valid!", "registration")
            is_valid = False


        if not (data['password'] == data['confirm_password']):
            flash("Passwords do not match", "registration")
            is_valid = False
        if not PASSWORD_REGEX.match(data['password']):
            flash("Password must include a number and be 8 characters long", "registration")
            is_valid = False


        if User.email_match(data):
            flash("Email already entered!", "registration")
            is_valid = False

        return is_valid








```