# main/models.py

from car_inventory import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(20), unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    book_length = db.Column(db.Integer)
    format = db.Column(db.String(50))

    def __repr__(self):
        return f'<Book {self.title} by {self.author}>'
