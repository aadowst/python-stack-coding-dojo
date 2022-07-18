# import the function that will return an instance of a connection

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import model_ninja

# model the class after the friend table from our database
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.ninjas = []
    # Now we use class methods to query our database



    @classmethod
    def save(cls, data ):

        query = "INSERT INTO dojos ( name ) VALUES ( %(name)s );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas').query_db( query, data )

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos
    
    @classmethod
    def get_one(cls, data):
        print("data inputed to get_one is:  ", data)
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return cls(result[0])


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


    @classmethod
    def edit(cls, data):
        query = "UPDATE dojos SET name = %(name)s WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas').query_db( query, data)


    @classmethod
    def delete(cls, id):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        connectToMySQL('dojos_and_ninjas').query_db(query, id)
        return
