import sqlite3
class Database:
    def __init__(self, database_name):
        self.database_name = database_name
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()
    def execute(self, sql, values):
        self.cursor.execute(sql, values)
    def commit(self):
        self.connection.commit()
    def rollback(self):
        self.connection.rollback()
    def fetchall(self):
        return self.cursor.fetchall()
    def fetchone(self):
        return self.cursor.fetchone()
    def add_book(self, book):
        self.execute("INSERT INTO books (title, author, price, category_id) VALUES (?, ?, ?, ?) ", (book.title, book.author, book.price, book.category_id))
        new_id = self.cursor.lastrowid
        return new_id
    def get_books(self):
        self.execute("SELECT * FROM books", ())
        return self.fetchall()
    def delete_book(self, id):
        self.execute("DELETE FROM books WHERE id = ?", (id,))
    def add_category(self, category):
        self.execute("INSERT INTO categories (name) VALUES(?)",(category.name,))
        new_id = self.cursor.lastrowid
        return new_id
    def get_categories(self):
        self.execute("SELECT * FROM categories", ())
        return self.fetchall()
    def update_price(self, book, new_price):
        self.execute(
            "UPDATE books SET price = ? WHERE id = ?",
            (new_price, book.id)
        )
