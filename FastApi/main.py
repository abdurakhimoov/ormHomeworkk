from fastapi import FastAPI, Query, Path
from pydantic import BaseModel

app = FastAPI()


@app.get("/students/{id}")
def get_student(id: int, course: str, year: int):
    return {
        "id": id,
        "course": course,
        "year": year
    }


class Order(BaseModel):
    product: str
    quantity: int
    price: float

@app.post("/orders/{id}")
def create_order(id: int, order: Order):
    total = order.quantity * order.price
    return {
        "id": id,
        "total": total
    }


class Book(BaseModel):
    title: str
    author: str
    price: float


@app.post("/books/")
def add_book(book: Book, discount: float = 0):
    discounted_price = book.price * (1 - discount / 100)
    return {
        "title": book.title,
        "author": book.author,
        "original_price": book.price,
        "discounted_price": discounted_price
    }

