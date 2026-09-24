from models import Book

def test_same_book():
    book1 = Book(1, "Python Basics", "John Smith", 500, 1)
    book2 = Book(2, "Python Basics", "John Smith", 600, 1)

    assert book1.is_same_book(book2)

def test_different_book():
    book1 = Book(1, "Python Basics", "Johan Smith", 500, 1)
    book2 = Book(2, "Python Advanced", "Johan Smith", 500, 1)

    assert not book1.is_same_book(book2)

def test_valid_price_positive():
    assert Book.is_valid_price(500)

def test_valid_price_negative():
    assert not Book.is_valid_price(-500)

def test_zero_price():
    assert Book.is_valid_price(0)
