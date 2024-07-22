# main/routes.py

from flask import Blueprint, render_template, redirect, url_for, flash, jsonify
from flask_login import login_required
from .forms import BookForm
from .models import Book
from car_inventory import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/books', methods=['GET', 'POST'])
@login_required
def books():
    form = BookForm()
    if form.validate_on_submit():
        new_book = Book(
            isbn=form.isbn.data,
            title=form.title.data,
            author=form.author.data,
            book_length=form.book_length.data,
            format=form.format.data
        )
        db.session.add(new_book)
        db.session.commit()
        flash('Book added successfully!', 'success')
        return redirect(url_for('main.books'))

    books = Book.query.all()
    return render_template('books.html', form=form, books=books)

# Other CRUD routes (get_book, update_book, delete_book) would be implemented similarly
