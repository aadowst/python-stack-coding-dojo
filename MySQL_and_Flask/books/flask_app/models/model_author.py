
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_book

class Author:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']

        self.favorite_books = []

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# #########################################################CLASS METHODS######################################################################3

# **********************************************************CREATE**********************************************************

    @classmethod
    def save(cls, data ):

        query = "INSERT INTO authors ( name) VALUES ( %(name)s);"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('books_sql_db').query_db( query, data )

    @classmethod
    def add_favorite(cls, data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        return connectToMySQL('books_sql_db').query_db( query, data )



# **********************************************************READ**************************************************************

# READ ALL

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"

        results = connectToMySQL('books_sql_db').query_db(query)
        list = []
        for entry in results:
            list.append( cls(entry) )
        return list
    

# READ ONE

    @classmethod
    def get_one(cls, id):
        query = "SELECT * FROM authors WHERE id = %(id)s;"
        results = connectToMySQL('books_sql_db').query_db(query, id)
        return cls(results[0])


# READ ALL AT ONE
    @classmethod
    def get_author_with_books_favorites(cls, data):
        query = "select * from authors left join favorites on authors.id = favorites.author_id left join books on favorites.book_id = books.id where authors.id = %(id)s;"
        results = connectToMySQL('books_sql_db').query_db(query, data)
        author_data = cls(results[0])
        
        for row_from_db in results:
            book_data = {
                "id": row_from_db["books.id"],
                "title": row_from_db["title"],
                "num_of_pages": row_from_db["num_of_pages"],
                "created_at": row_from_db["books.created_at"],
                "updated_at": row_from_db["books.updated_at"]
            }
            author_data.favorite_books.append(model_book.Book(book_data))
        return author_data


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
