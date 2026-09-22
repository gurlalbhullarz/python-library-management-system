class Book:
    def __init__(self, id, title, author, price, category_id):
        self.id = id
        self.title = title
        self.author = author
        self.price = price
        self.category_id = category_id

#display_info about books
    def display_info(self):
        print(f"Book id: {self.id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price:.2f}")
        #print(f"Category ID: {self.category_id}")

    def update_price(self, new_price):
        self.price = new_price
        print(f"Updated price for '{self.title}' is now ${self.price:.2f}")

    def is_same_book(self, other_book):
        return self.title.lower() == other_book.title.lower() and self.author.lower() == other_book.author.lower()
    
    @staticmethod

    def is_valid_price(price):
        if price >=0:
            return price
class Category:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def display_info(self):
        print(f"Category ID: {self.id}")
        print(f"Category: {self.name}")