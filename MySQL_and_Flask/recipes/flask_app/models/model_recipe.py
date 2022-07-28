from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

from flask_app.models import model_user

DATABASE = "recipes"

class Recipe:
    def __init__( self , data ):

        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under = data['under']
        self.cooked = data['cooked']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save_recipe(cls, data ):

        query = "INSERT INTO recipes ( name, description, instructions, under, cooked, user_id) VALUES ( %(name)s, %(description)s, %(instructions)s, %(under)s, %(cooked)s, %(user_id)s );"

        return connectToMySQL(DATABASE).query_db( query, data )

    

    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes JOIN users on recipes.user_id = users.id;"

        results = connectToMySQL(DATABASE).query_db(query)
        all_recipes = []

        for dict in results:
            recipe = cls(dict)
            user_data = {
                "id" : dict["users.id"],
                "created_at" : dict["users.created_at"],
                "updated_at" : dict["users.updated_at"],
                "first_name": dict["first_name"],
                "last_name": dict["last_name"],
                "email": dict["email"],
                "password": dict["password"]
            }
            user = model_user.User(user_data)
            recipe.submitter = user
            all_recipes.append(recipe)

        return all_recipes

    @classmethod
    def get_one_recipe(cls, id):
        query = "SELECT * FROM recipes join users on recipes.user_id = users.id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, id)
        print(results)
        return (results[0])

    # @classmethod
    # def get_one_recipe(cls, id):
    #     query = "SELECT * FROM recipes WHERE id = %(id)s;"
    #     results = connectToMySQL(DATABASE).query_db(query, id)
    #     return cls(results[0])

    @classmethod
    def edit_recipe_action(cls, data):
        print("The submitted data is:  ", data)
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, under = %(under)s, cooked = %(cooked)s, user_id = %(user_id)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db( query, data)

    @classmethod
    def delete(cls, id):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        connectToMySQL(DATABASE).query_db(query, id)
        return

    @staticmethod
    def validate_input(data):
        is_valid = True
        if (len(data['name'])<3):
            flash("name must be at least 3 characters")
            is_valid = False
        if (len(data['description'])<3):
            flash("description must be at least 3 characters")
            is_valid = False
        if (len(data['instructions'])<3):
            flash("instructions must be at least 3 characters")
            is_valid = False
        if not "under" in data:
            flash("select over or under 30 minutes")
            is_valid = False
        if (len(data['cooked'])<3):
            flash("enter when you cooked/made the dish")
            is_valid = False
        return is_valid