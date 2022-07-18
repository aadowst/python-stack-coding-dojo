
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_author

class Book:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.favorited_by = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# #########################################################CLASS METHODS######################################################################3

# **********************************************************CREATE**********************************************************

    @classmethod
    def save(cls, data ):

        query = "INSERT INTO books ( title, num_of_pages ) VALUES ( %(title)s, %(num_of_pages)s);"

        return connectToMySQL('books_sql_db').query_db( query, data )


# **********************************************************READ**************************************************************

# READ ALL

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_sql_db').query_db(query)
        list = []
        for entry in results:
            list.append( cls(entry) )
        return list
    
    @classmethod
    def get_all_not_favorites(cls, id):
        query = "select * from books where books.id not in (select favorites.book_id from favorites where author_id = %(id)s);"
        results = connectToMySQL('books_sql_db').query_db(query, id)
        book_list = []
        for row_from_db in results:
            book_data = {
                "id": row_from_db["id"],
                "title": row_from_db["title"],
                "num_of_pages": row_from_db["num_of_pages"],
                "created_at": row_from_db["created_at"],
                "updated_at": row_from_db["updated_at"]
            }
            book_list.append(Book(book_data))
        
        return book_list

# READ ONE

    @classmethod
    def get_one(cls, id):
        query = "SELECT * FROM books WHERE id = %(id)s;"
        results = connectToMySQL('books_sql_db').query_db(query, id)
        return cls(results[0])


    @classmethod
    def get_book_with_author_favorites(cls, data):
        query = "select * from books left join favorites on books.id = favorites.book_id left join authors on favorites.author_id = authors.id where books.id = %(id)s;"

        results = connectToMySQL('books_sql_db').query_db(query, data)

        book_data = cls(results[0])

        for row_from_db in results:
            author_data = {
                "id": row_from_db["authors.id"],
                "name": row_from_db["name"],
                "created_at": row_from_db["authors.created_at"],
                "updated_at": row_from_db["authors.updated_at"]
            }
            book_data.favorited_by.append(model_author.Author(author_data))
        return book_data




