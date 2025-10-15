from sqlalchemy.orm import Session
from models.book import Book
from schemas.book import BookBase


def create_book(db: Session,book: BookBase):
    try:
        db_book = Book(title=book.title, author=book.author)
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book
    except Exception as e:
        db.rollback()
        raise Exception(e)

def get_books(db: Session):
    try:
        books = db.query(Book).all()
        return books
    except Exception as e:
        db.rollback()
        raise Exception(e)

def get_book_by_id(db: Session, boo_id: int):
    try:
        book = db.query(Book).filter(Book.id == boo_id).first()
        return book
    except Exception as e:
        db.rollback()
        raise Exception(e)

def update_book(db: Session, boo_id: int, book: BookBase):
    try:
        data = db.query(Book).filter(Book.id == boo_id).first()
        data.title = book.title
        data.author = book.author
        db.commit()
        db.refresh(book)
        return book
    except Exception as e:
        db.rollback()
        raise Exception(e)

def delete_book(db: Session, book_id: int):
    try:
        book = db.query(Book).filter(Book.id == book_id).first()
        db.delete(book)
        db.commit()
        return book
    except Exception as e:
        db.rollback()
        raise Exception(e)
