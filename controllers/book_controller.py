from http.client import HTTPException

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from db.database import get_db
from schemas.book import BookResponse, BookBase
from services import book_service
from util.response import success, not_found

router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/", response_model=BookResponse)
def create(book: BookBase, db: Session = Depends(get_db)):
    db_book = book_service.create_book(db, book)
    return db_book

@router.get("/", response_class=JSONResponse)
def read_books(db: Session = Depends(get_db)):
    try:
        books = book_service.get_books(db)
        dict_new = [BookResponse.model_validate(b).model_dump() for b in books]
        return success(dict_new)
    except HTTPException as e:
        db.rollback()
        return not_found(f"Exception: {e}")

@router.get("/{book_id}", response_class=JSONResponse)
def read_book(db: Session = Depends(get_db), book_id: int=0):
    try:
        book = book_service.get_book_by_id(db, book_id)
        if not book:
            return not_found(f"Book with id={book_id} not found")
        dict_book = {
            "id": book_id,
            "title": book.title,
            "author": book.author,
        }
        return success(dict_book)
    except HTTPException as e:
        db.rollback()
        return not_found(f"Book with id={book_id} not found")
