from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.models.model_author import Author
from flask_app.models.model_book import Book




# *************************CREATE*******************************

# ADD TO DB ACTION
@app.route('/addbook', methods=["POST"])
def add_one_book():

    id = Book.save(request.form)
    return redirect(f"/books/{id}")


# should this be it its own controller??? and should favorites also have its own model???
@app.route('/addfavoriteauthor', methods=["Post"])
def author_favorites_book():

    Author.add_favorite(request.form)
    book_id = request.form["book_id"]
    print(book_id)
    return redirect (f"/books/{book_id}")
# ********************************READ*******************************************


# READ ONE
@app.route('/books/<int:id>')
def one_book(id):
    favorited_by = Book.get_book_with_author_favorites({"id": id})
    not_favorited_by = Author.get_all_not_favorited_by({"id":id})
    book_id = id
    return render_template("books_one.html", favorited_by = favorited_by, not_favorited_by=not_favorited_by, book_id=book_id)

# READ ALL

@app.route("/books")
def all_books():

    all_data = Book.get_all()

    return render_template("books_all.html", all_data=all_data)