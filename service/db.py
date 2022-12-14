import enum
from typing import Dict

class Book:
    def __init__(self, isbn, title, author, genre, publishing_year):
        self.ISBN = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.publishing_year = publishing_year

# Enum for the genre field
class Genre(enum.Enum):
    UNKNOWN = 1
    FICTION = 2
    NON_FICTION = 3
    POETRY = 4

# Hardcoded "database" of books
books: Dict[str, Book] = {
    "123456": Book("123456", "Harry Potter and the Sorcerer's Stone", "J.K. Rowling", Genre.FICTION, 1997),
    "234567": Book("234567", "The Hitchhiker's Guide to the Galaxy", "Douglas Adams", Genre.FICTION, 1979),
    "345678": Book("345678", "Murder on the Orient Express", "Agatha Christie", Genre.UNKNOWN, 1934)
}