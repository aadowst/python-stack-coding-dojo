# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

# model the class after the friend table from our database
class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
    # Now we use class methods to query our database


    # class method to save our ninja to the database
    @classmethod
    def save(cls, data ):

        query = "INSERT INTO ninjas ( first_name , last_name , age, dojo_id) VALUES ( %(first_name)s , %(last_name)s , %(age)s, %(dojo_id)s);"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas').query_db( query, data )

    
    @classmethod
    def ninjas_at_one_dojo(cls, dojo_id):
#  query = "SELECT * FROM ninjas JOIN dojos on dojos.id = ninjas.dojo_id WHERE ninjas.dojo_id = %(dojo_id)s;"
        query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query, dojo_id)
        print(results)
        ninjas = []
        # Iterate over the db results and create instances of friends with cls.
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas


    @classmethod
    def edit(cls, data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas').query_db( query, data)


    @classmethod
    def delete(cls, id):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        connectToMySQL('dojos_and_ninjas').query_db(query, id)
        return


