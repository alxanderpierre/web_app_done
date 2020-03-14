from flask import Blueprint, jsonify, request, render_template

book_routes = Blueprint("book_routes", __name__)

@book_routes.route("/books.json")
def list_books():
    books = [
    {"id": 1, "titles": "Book 1"},
    {"id": 2, "title ": "Book 2"},
    {"id": 2, "title ": "Book 3"}
    ]
    return jsonify(books)


@book_routes.route("/books")
def list_books_for_humans():
    books = [
    {"id": 1, "titles": "Book 1"},
    {"id": 2, "title ": "Book 2"},
    {"id": 2, "title ": "Book 3"}
    ]
    return render_template("books.html", message= "here are some books", books=books)

@book_routes.route("/books/new")
def new_book():
    return render_template("new_book.html")

@book_routes.route("/books/create", methods=["POST"])
def create_book():
    print("FROM DATA:", dict(request.form))

    return jsonify({
    "message": "Book created ok (TODO)",
    "book": dict(request.form)
    })
