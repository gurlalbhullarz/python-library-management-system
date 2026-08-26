import sqlite3
def connect_db():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    return conn, cursor

def create_database():
    conn,cursor = connect_db()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS books
                   (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT,
                   author TEXT,
                   price REAL
                   )

                   """)
    conn.commit()
    conn.close()
def add_book():
    conn, cursor = connect_db()
    title = input("Enter Book Title: ")
    author = input("Enter the author name: ")
    try:
        price = float(input("Enter the book price: "))
    except ValueError:
        print("Please enter a correct price value")
        conn.close()
        return
    cursor.execute("SELECT id, name FROM categories")
    categories = cursor.fetchall()
    print("Available Categories:")
    for category in categories:
        print(f"ID: {category[0]}, Name: {category[1]}")
    try:
       choice = int(input("Choose a category: "))
    except ValueError:
        print("Please enter a valid category ID.")
        conn.close()
        return    
    cursor.execute(
    "SELECT id FROM categories WHERE id = ?",
    (choice,)
)
    category = cursor.fetchone()
    if category is None:
        print("Invalid category.")
        conn.close()
        return
    cursor.execute(
    """
    INSERT INTO books (title, author, price, category_id)
    VALUES (?, ?, ?, ?)
    """,
    (title, author, price, choice)
)
    conn.commit()
    conn.close()
    print("Book added successfully!")
def view_books():
    conn, cursor = connect_db()
    cursor.execute("""SELECT books.id, books.title, books.author, books.price, categories.name
    FROM books
    JOIN categories
    ON books.category_id = categories.id """)
    books = cursor.fetchall()
    conn.close()
    if books:
        print("Books in the library:")
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Price: ${book[3]:.2f} , Category: {book[4]}")
    else:
        print("No books found in the library.")
def search_book():
    conn, cursor = connect_db()
    search_title = input("Enter the title of the book to search: ")
    cursor.execute("""SELECT books.id, books.title, books.author, books.price, categories.name
    FROM books
    JOIN categories
    ON books.category_id = categories.id
    WHERE books.title = ?""", (search_title,))
    book = cursor.fetchone()
    if book:
        print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Price: ${book[3]:.2f} , Category: {book[4]}")
    else:
        print("Book not found.")
    conn.close()
def update_price():
    conn, cursor = connect_db()
    try:
        book_id = int(input("Enter the Book ID: "))
    except ValueError:
        print("Please enter a valid ID.")
        conn.close()
        return
    try:
        new_price = float(input("Enter the new price: "))
    except ValueError:
        print("Please enter a valid price")
        conn.close()
        return
    cursor.execute("UPDATE books SET price = ? WHERE id = ?", (new_price, book_id))
    if cursor.rowcount > 0:
        print("Price updated successfully!")
    else:
        print("Book not found.")
    conn.commit()
    conn.close()
def delete_book():
    conn, cursor = connect_db()
    try:
        book_id = int(input("Enter the ID of the book you want to delete: "))
    except ValueError:
        print("Please enter a valid ID.")
        conn.close()
        return
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    if cursor.rowcount > 0:
        print("Book deleted successfully!")
    else:
        print("Book not found.")
    conn.commit()
    conn.close() 
def expensive_book():
    conn, cursor = connect_db()
    cursor.execute("""SELECT books.id, books.title, books.author, books.price, categories.name
    FROM books
    JOIN categories
    ON books.category_id = categories.id
    ORDER BY books.price DESC
    LIMIT 1;""")
    expensivebook = cursor.fetchone()
    if expensivebook:
        print("Most Expensive Book:")
        print(f"ID: {expensivebook[0]}, Title: {expensivebook[1]}, Author: {expensivebook[2]}, Price: ${expensivebook[3]:.2f} , Category: {expensivebook[4]}")
    else:
        print("No books found")
    conn.close()
def cheapest_book():
    conn, cursor = connect_db()
    cursor.execute("""SELECT books.id, books.title, books.author, books.price, categories.name
    FROM books
    JOIN categories
    ON books.category_id = categories.id
    ORDER BY books.price ASC
    LIMIT 1;""")
    cheapestbook = cursor.fetchone()
    if cheapestbook:
        print("Cheapest Book:")
        print(
            f"ID: {cheapestbook[0]}, Title: {cheapestbook[1]}, Author: {cheapestbook[2]}, Price: ${cheapestbook[3]:.2f} , Category: {cheapestbook[4]}")
    else:
        print("No books found")
    conn.close()

def main():
    create_database()
    create_categories_table()
    migrate_books_table()
    while True:
        print("""===== Library Management System =====
1. Add Book
2. View Books
3. Search Book
4. Update Price
5. Assign Category
6. Delete Book
7. Most Expensive Book
8. Cheapest Book
9. Add Category
10. Exit""")
        try:
            user_input = int(input("Choose from 1-10: "))
        except ValueError:
            print("Please enter a number.")
            continue
        if user_input == 1:
            add_book()
            pause()
        elif user_input == 2:
            view_books()
            pause()
        elif user_input == 3:
            search_book()
            pause()
        elif user_input == 4:
            update_price()
            pause()
        elif user_input == 5:
            assign_category()
            pause()
        elif user_input == 6:
            delete_book()
            pause()
        elif user_input == 7:
            expensive_book()
            pause()
        elif user_input == 8:
            cheapest_book()
            pause()
        elif user_input == 9:
            add_category()
            pause()
        elif user_input == 10:      
            print("Exiting....")
            break
        else:
            print("Please choose a valid option")

def create_categories_table():
    conn, cursor = connect_db()

    cursor.execute("""
      CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE)
""")

    conn.commit()
    conn.close()
def add_category():
    conn, cursor = connect_db()

    category = input("Enter category name: ").strip().upper()

    try:
        cursor.execute(
            "INSERT INTO categories (name) VALUES (?)",
            (category,)
        )
        conn.commit()
        print("Category added successfully!")
        conn.close()
    except sqlite3.IntegrityError:
        print("Category already exists.")
        conn.rollback()
        conn.close()
def assign_category():
    conn, cursor = connect_db()

    try:
        book_id = int(input("Enter the Book ID: "))
    except ValueError:
        print("Please enter a valid ID.")
        conn.close()
        return

    cursor.execute("SELECT id, name FROM categories")
    categories = cursor.fetchall()
    print("Available Categories:")
    for category in categories:
        print(f"ID: {category[0]}, Name: {category[1]}")

    try:
        choice = int(input("Choose a category: "))
    except ValueError:
        print("Please enter a valid category ID.")
        conn.close()
        return

    cursor.execute(
        "SELECT id FROM categories WHERE id = ?",
        (choice,)
    )
    category = cursor.fetchone()
    if category is None:
        print("Invalid category.")
        conn.close()
        return

    cursor.execute(
        "UPDATE books SET category_id = ? WHERE id = ?",
        (choice, book_id)
    )
    if cursor.rowcount > 0:
        print("Category assigned successfully!")
    else:
        print("Book not found.")

    conn.commit()
    conn.close()
def migrate_books_table():
    conn, cursor = connect_db()
    conn.execute("PRAGMA foreign_keys = ON")
    cursor.execute("PRAGMA table_info(books)")
    columns = cursor.fetchall()
    column_names = [column[1] for column in columns]
    if "category_id" not in column_names:
        cursor.execute("""
            ALTER TABLE books
            ADD COLUMN category_id INTEGER
        """)

    cursor.execute("PRAGMA foreign_key_list(books)")
    foreign_keys = cursor.fetchall()
    if foreign_keys:
        print("Foreign key already exists. Migration not needed.")
        conn.close()
        return
    
    cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
    AND name = ?
    """, ("books_new",))
    result = cursor.fetchone()
    if result:
        print("books_new already exists. Using existing table.")
    else:
        cursor.execute("""
        CREATE TABLE books_new (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            price REAL,
            category_id INTEGER,
            FOREIGN KEY (category_id)
            REFERENCES categories(id)
        )
    """)
    try:
        cursor.execute("""
        INSERT INTO books_new (id, title, author, price, category_id)
        SELECT id, title, author, price, category_id
        FROM books
        """)
        cursor.execute("DROP TABLE books")
        cursor.execute("""
    ALTER TABLE books_new
    RENAME TO books
    """)
    
        conn.commit()
        print("Migration completed successfully.")
        conn.close()
    except Exception as e:
        conn.rollback()
        print(f"Migration failed: {e}")
        conn.close()

def pause():
    input("\nPress Enter to continue...")
if __name__ == "__main__":
    main()
