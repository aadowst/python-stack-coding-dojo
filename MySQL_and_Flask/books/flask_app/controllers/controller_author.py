from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.models.model_author import Author
from flask_app.models.model_book import Book




# *************************CREATE*******************************

# ADD TO DB ACTION
@app.route('/addauthor', methods=["POST"])
def add_one_author():

    id = Author.save(request.form)
    return redirect(f"/authors/{id}")


# should this be it its own controller??? and should favorites also have its own model???
@app.route('/addfavorite', methods=["Post"])
def favorite_book():
    print(request.form['author_id'], request.form["book_id"])
    Author.add_favorite(request.form)
    author_id = request.form["author_id"]
    return redirect (f"/authors/{author_id}")


# ********************************READ*******************************************


# READ ONE
@app.route('/authors/<int:id>')
def one_author(id):
    favorites = Author.get_author_with_books_favorites({"id": id})
    not_favorites = Book.get_all_not_favorites({"id":id})
    author_id = id
    return render_template("authors_one.html", favorites = favorites, not_favorites=not_favorites, author_id=author_id)

# READ ALL

@app.route("/authors")
def all_authors():

    all_data = Author.get_all()
    print(all_data)
    return render_template("authors_all.html", all_data=all_data)