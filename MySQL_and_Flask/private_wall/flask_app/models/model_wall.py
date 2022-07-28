



from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

from flask_app.models import model_user

class Wall:
    def __init__( self , data ):

        self.id = data['id']
        self.message = data['message']

        # DOUBLE CHECK THESE NAMES
        self.sender_id = data['sender_id']
        self.recipient_id = data['recipient_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    @classmethod
    def create_message(cls, data ):

        query = "INSERT INTO messages ( message, recipient_id, sender_id ) VALUES ( %(message)s, %(recipient_id)s, %(sender_id)s );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('login_reg').query_db( query, data )

    # @classmethod
    # def add_to_linking_table(cls, data ):
    #     query = "INSERT INTO users_messages ( message_id, recipient_id, sender_id ) VALUES ( %(message_id)s, %(recipient_id)s, %(sender_id)s );"
    #     # data is a dictionary that will be passed into the save method from server.py
    #     return connectToMySQL('login_reg').query_db( query, data )


    @classmethod
    def get_all_user_messages(cls, data):
        query = "SELECT * FROM messages join users on messages.sender_id = users.id where recipient_id = %(recipient_id)s;"
        results = connectToMySQL('login_reg').query_db(query, data)
        if not results:
            return {}
        if results:
            all_messages = []
        # Iterate over the db results and create instances of friends with cls.
            for dict in results:

                message = cls(dict)
                user_data = {
                    "id": dict["sender_id"],
                    "first_name": dict["first_name"],
                    "last_name": dict["last_name"],
                    "email": dict["email"],
                    "password": dict["password"],
                    "created_at": dict["users.created_at"],
                    "updated_at":dict["users.updated_at"]
                }
                user = model_user.User(user_data)
                message.sender = user
            # is here where i call the users class to get their names?
                all_messages.append(message)
                print("appended instance of user to message model_wall line 58")
        return all_messages
    
    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM ;"
    #     results = connectToMySQL('login_reg').query_db(query)
    #     all_users = []
    #     # Iterate over the db results and create instances of friends with cls.
    #     for user in results:
    #         all_users.append( cls(user) )
    #     return all_users

    @classmethod
    def count_messages (cls, data):
        print("data inputed to get_one is:  ", data)
        query = "Select count(id) from messages where sender_id = %(sender_id)s;"
        result = connectToMySQL('login_reg').query_db(query, data)
        number = result[0]["count(id)"]
        return number

    # @classmethod
    # def email_match(cls, data):
    #     print("email to be found is:  ", data)
    #     query = "SELECT * FROM users WHERE email = %(email)s;"
    #     result = connectToMySQL('login_reg').query_db(query, data)
    #     print("the result is:  ",result)
    #     if not result:
    #         return False
    #     return cls(result[0])


    # @classmethod
    # def edit(cls, data):
    #     query = "UPDATE users SET name = %(name)s WHERE id = %(id)s;"
    #     return connectToMySQL('login_reg').query_db( query, data)


    @classmethod
    def delete(cls, id):
        query = "DELETE FROM messages WHERE id = %(id)s;"
        connectToMySQL('login_reg').query_db(query, id)
        return

