from database import Database
from library import Library
from models import Book, Category
def main():
    database = Database("library.db")
    library = Library(database)

    library.load_books()
    library.load_categories()
    library.view_books()

if __name__ == "__main__":
    main()
