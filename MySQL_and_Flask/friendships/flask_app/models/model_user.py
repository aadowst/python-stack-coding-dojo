

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.friends = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save_user(cls, data ):
        query = "INSERT INTO users ( first_name, last_name ) VALUES ( %(first_name)s, %(last_name)s );"

        return connectToMySQL('friendships_db').query_db( query, data )

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('friendships_db').query_db(query)
        list = []
        for entry in results:
            list.append( cls(entry) )
        return list


    @classmethod
    def get_all_friendships(cls):
        query = "SELECT * FROM users JOIN friendships on users.id = friendships.user_id LEFT JOIN users as friend on friendships.friend_id = friend.id;"
        results = connectToMySQL('friendships_db').query_db(query)
        # results are all entry
        print(results)
        list_of_friendships = []
        for row_in_db in results:
            # this cycles through all users that are returned

            user = cls(row_in_db)
            # this creates an instance of the class with the user's id
            entry = {
                "id": row_in_db["friend.id"],
                "first_name": row_in_db["friend.first_name"],
                "last_name": row_in_db["friend.last_name"],
                "created_at": row_in_db["friend.created_at"],
                "updated_at": row_in_db["friend.updated_at"],
                
            }
            friend = cls(entry)
            # this creates instances for each friend associated with that user
            user.friend = friend
            list_of_friendships.append(user )
        return list_of_friendships




class Friendship:
    def __init__( self , data ):
        self.id = data['id']
        # self.user_id = data['user_id']
        # self.friend_id = data['friend_id']
        self.list = []
        # self.created_at = data['created_at']
        # self.updated_at = data['updated_at']

    # @classmethod
    # def get_all_friendships(cls):
    #     query = "SELECT users.first_name as user_first_name, users.last_name as user_last_name, friend.first_name as friend_first_name, friend.last_name as friend_last_name FROM users JOIN friendships on users.id = friendships.user_id LEFT JOIN users as friend on friendships.friend_id = friend.id;"
    #     results = connectToMySQL('friendships_db').query_db(query)
    #     list = []
    #     for entry in results:
    #         list.append( cls(entry) )
    #     return list

