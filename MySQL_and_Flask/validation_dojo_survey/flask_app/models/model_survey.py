# import the function that will return an instance of a connection

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# model the class after the friend table from our database
class Survey:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # Now we use class methods to query our database



    @classmethod
    def save(cls, data ):

        query = "INSERT INTO dojos ( name, location, language, comment ) VALUES ( %(name)s, %(location)s, %(language)s, %(comment)s );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojo_survey_schema').query_db( query, data )

    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM dojos;"
    #     # make sure to call the connectToMySQL function with the schema you are targeting.
    #     results = connectToMySQL('dojo_survey_schema').query_db(query)
    #     # Create an empty list to append our instances of friends
    #     dojos = []
    #     # Iterate over the db results and create instances of friends with cls.
    #     for dojo in results:
    #         dojos.append( cls(dojo) )
    #     return dojos
    

    @classmethod
    def get_one(cls, data):
        print("data inputed to get_one is:  ", data)
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL('dojo_survey_schema').query_db(query, data)
        return cls(result[0])

    # @classmethod
    # def edit(cls, data):
    #     query = "UPDATE dojos SET name = %(name)s WHERE id = %(id)s;"
    #     return connectToMySQL('dojo_survey_schema').query_db( query, data)


    # @classmethod
    # def delete(cls, id):
    #     query = "DELETE FROM dojos WHERE id = %(id)s;"
    #     connectToMySQL('dojo_survey_schema').query_db(query, id)
    #     return

    @staticmethod
    def validate_comment(comment):
        is_valid = True

        if (len(comment['name']) <3):
            flash("Name must be at least 3 characters")
            is_valid = False
        if " " not in comment['name']:
            flash("Include your full name")
            is_valid = False
        if (len(comment['location'])<3):
            flash("Location must be at least  3 characters")
            is_valid = False
        if (len(comment['language'])<3):
            flash("Language must be at least 3 characters")
            is_valid = False
        if (len(comment['comment'])<3):
            flash("Comments must be at least 3 characters")
            is_valid = False
        return is_valid