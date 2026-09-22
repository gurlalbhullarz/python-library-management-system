import sqlite3
from models import Book, Category
from database import Database
class Library:
    def __init__(self, database):
        self.database = database
        self.books = []
        self.categories = []
    def add_book(self, book):
        for existing_book in self.books:
            if existing_book.is_same_book (book):
                print("This book is already exists.")
                return
        try:
            new_id = self.database.add_book(book)
            self.database.commit()
        except sqlite3.Error as e:
            print(f"Error occurred while adding book: {e}")
            self.database.rollback()
        else:
            book.id = new_id
            self.books.append(book)
    def view_books(self):
        for book in self.books:
            self.display_book_info(book)
    def search_book(self, keyword):
        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                return book
        return None
    def search_books(self, keyword):
        matches = []
        for books in self.books :
            if keyword.lower() in books.title.lower() or keyword.lower() in books.author.lower() :
                matches.append(books)
        return matches 
    def delete_book(self, id):
        for book in self.books:
            if book.id == id:
                try:
                    self.database.delete_book(id)
                    self.database.commit()

                except sqlite3.Error as e:
                    self.database.rollback()
                    print(f"Database error: {e}")

                else:
                    self.books.remove(book)
                    print(f"Book with ID {id} has been deleted.")

                return

        print(f"Book with ID {id} not found in the library.")

    def expensive_book(self):
        expensive_book = max(self.books, key=lambda book: book.price)
        return expensive_book
    def cheapest_book(self):
        cheapest_book = min(self.books, key=lambda book: book.price)
        return cheapest_book
    def load_books(self):
        self.books.clear()
        rows = self.database.get_books()

        for row in rows:
            book = Book(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4]
            )
            self.books.append(book)
    def update_price(self, book, new_price):
        if not Book.is_vaild_price(new_price):
            print("Please enter a valid price")
            return
        try:
            self.database.update_price(book, new_price)
            self.database.commit()

        except sqlite3.Error as e:
            self.database.rollback()
            print(f"Database error: {e}")

        else:
            book.update_price(new_price)
    def load_categories(self):
        self.categories.clear()
        rows = self.database.get_categories()
        for row in rows:
            category = Category(
                row[0],
                row[1]
            )
            self.categories.append(category)
    def add_category(self, category):
        try:
            new_id = self.database.add_category(category)
            self.database.commit()
        except sqlite3.Error as e:
            print(f"Error occured while adding category: {e}")
            self.database.rollback()
        else:
            category.id = new_id
            self.categories.append(category)
    def get_book_category(self, book):
        for category in self.categories:
            if book.category_id == category.id :
                return category
        return None
    def display_book_info(self, book):
        book.display_info()
        category = self.get_book_category(book)
        if category:
            category.display_info()
