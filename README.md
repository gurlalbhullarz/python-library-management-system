# 📚 Library Management System

A command-line Library Management System built with **Python and SQLite**.

The project started as a basic CRUD application and was later evolved into a relational database application by migrating the existing database structure without deleting the existing data.

## 🚀 Features

* Add, view, search, and delete books
* Update book prices
* Add and manage categories
* Assign categories to existing books
* Find the most expensive and cheapest book
* SQLite database
* Foreign-key relationships
* SQL `JOIN` queries
* Input validation
* Database migration while preserving existing data

## 🗄️ Database Design

The project contains two related tables:

### `books`

* `id`
* `title`
* `author`
* `price`
* `category_id`

### `categories`

* `id`
* `name`

### Relationship

```text
books.category_id → categories.id
```

## 🔄 Database Migration

The original version of the project did not have categories.

Instead of deleting the existing database and starting again, I migrated the existing structure while preserving the existing book records.

The migration involved:

1. Adding `category_id`
2. Creating the new table structure
3. Transferring existing records using `INSERT ... SELECT`
4. Replacing the old table
5. Renaming the migrated table
6. Adding the foreign-key relationship

This allowed the existing data to remain intact while evolving the database design.

## 🛠️ Technologies

* Python
* SQLite
* SQL

## ▶️ How to Run

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd library-management-system
```

Run the application:

```bash
python library_management.py
```

The SQLite database will be created automatically.

## 📸 Project

The application runs through a command-line interface where users can manage books and categories.

## 🔮 Next Version

The next version of this project will focus on:

* Object-Oriented Programming
* Better application architecture
* More advanced features
