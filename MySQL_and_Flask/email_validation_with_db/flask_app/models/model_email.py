# import the function that will return an instance of a connection
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# model the class after the friend table from our database
class Email:
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # Now we use class methods to query our database



    @classmethod
    def save(cls, data ):

        query = "INSERT INTO emails ( email ) VALUES ( %(email)s );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('email_validation').query_db( query, data )

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL('email_validation').query_db(query)
        all_emails = []
        # Iterate over the db results and create instances of friends with cls.
        for email in results:
            all_emails.append( cls(email) )
        return all_emails
    

    @classmethod
    def get_one(cls, data):
        print("data inputed to get_one is:  ", data)
        query = "SELECT * FROM emails WHERE id = %(id)s;"
        result = connectToMySQL('email_validation').query_db(query, data)
        return cls(result[0])

    @classmethod
    def email_match(cls, data):
        print("email to be found is:  ", data)
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        result = connectToMySQL('email_validation').query_db(query, data)
        print("the result is:  ",result)
        return result


    # @classmethod
    # def edit(cls, data):
    #     query = "UPDATE emails SET name = %(name)s WHERE id = %(id)s;"
    #     return connectToMySQL('email_validation').query_db( query, data)


    @classmethod
    def delete(cls, id):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        connectToMySQL('email_validation').query_db(query, id)
        return


    @staticmethod
    def validate_email(email):
        is_valid = True
        if (len(email['email'])<1):
            flash("please enter an email address")
            is_valid = False
        if not EMAIL_REGEX.match(email['email']):
            flash("Email is not valid!")
            is_valid = False
        if Email.email_match(email):
            flash("Email already entered!")
            is_valid = False
        return is_valid