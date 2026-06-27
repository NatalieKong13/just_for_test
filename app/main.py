from fastapi import FastAPI

app = FastAPI()


books = [
    {"id": 1, "title": "The Pragmatic Programmer"},
    {"id": 2, "title": "Clean Code"}
]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"version": "1.0.0"}

@app.get("/books")
def get_books():
    return books

@app.post("/books")
def add_book(book: dict):
    books.append(book)
    return book