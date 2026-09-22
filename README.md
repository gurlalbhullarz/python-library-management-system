# 📚 Python Library Management System

A Python-based Library Management System built with **Python and SQLite**.

This project is being developed step by step to apply Python programming concepts in a practical application — starting from a procedural implementation and gradually moving toward **Object-Oriented Programming, modular architecture, testing, and advanced features**.

---

## 🚀 Project Journey

The project is intentionally developed incrementally rather than being rewritten from scratch. Existing database data is preserved while new concepts and architecture are introduced.

### Phase 1 — Procedural Version ✅

The project originally started as a procedural Python application using functions and SQLite.

Implemented:

* Book management
* Category management
* CRUD operations
* SQLite database integration
* Book searching
* Price updates
* Database transactions
* Commit and rollback handling

---

### Phase 2 — Object-Oriented Programming ✅

The procedural application was gradually refactored into an Object-Oriented design while keeping the existing database and data.

Implemented:

* `Book` class
* `Category` class
* `Library` class
* `Database` class
* Instance methods
* Static methods
* Object interaction
* Composition
* Dependency injection
* Encapsulation

---

### Phase 3 — Modular Architecture ✅

The application was separated into dedicated modules to make the code easier to maintain and extend.

Current structure:

```text
python-library-management-system/
│
├── main.py
├── models.py
├── library.py
├── database.py
├── library.db
└── README.md
```

### Responsibilities

**`models.py`**

* `Book`
* `Category`

**`database.py`**

* SQLite connection
* Database queries
* CRUD database operations
* Commit and rollback

**`library.py`**

* Library business logic
* Book management
* Category management
* Searching
* Validation

**`main.py`**

* Application entry point
* Initializes the database and library

---

## 🔐 Validation & Data Integrity

The project currently includes:

* Price validation
* Duplicate-book detection
* Title + author comparison
* Case-insensitive duplicate checking
* Database commit and rollback handling
* Existing database preservation

Duplicate books are currently identified using the **book title and author**, rather than price.

---

## 🗄️ Database

The application uses **SQLite** for persistent data storage.

The existing `library.db` database is being reused throughout the project's development instead of creating a new database during the OOP refactoring.

This allows the project to evolve while preserving previously stored data.

---

## 🧪 Testing — Next Step

The next development stage is to introduce automated testing.

Planned:

* Unit tests for models
* Database operation tests
* Library operation tests
* Validation tests
* Duplicate-book tests
* Error handling tests
* Rollback tests
* Testing with a separate test database

---

## 📖 Upcoming Features

After testing, the project will continue toward a more complete library system.

Planned features include:

* Member management
* Borrowing and returning books
* Book availability
* Due dates
* Overdue tracking
* Improved database relationships
* Reporting and statistics
* More advanced application architecture
* SQLAlchemy
* API/backend integration

---

## 🛠️ Technologies

* **Python**
* **SQLite**
* **SQL**
* **Object-Oriented Programming**
* **Git & GitHub**

---

## 🎯 Project Goal

The goal of this project is not only to build a Library Management System.

It is also a practical learning project where I progressively apply:

```text
Python Fundamentals
        ↓
Procedural Programming
        ↓
SQLite & SQL
        ↓
Object-Oriented Programming
        ↓
Modular Architecture
        ↓
Validation & Data Integrity
        ↓
Automated Testing
        ↓
Advanced Features
        ↓
SQLAlchemy
        ↓
API / Backend Development
```

Each stage builds on the previous one while keeping the project functional and preserving existing data.

---

## 👨‍💻 Development Approach

This project is being developed **step by step**.

Instead of creating a large application all at once, each stage introduces new programming and software-development concepts into the existing project.

The Git history documents this progression from the original procedural implementation to the current Object-Oriented and modular architecture.

---

## 📌 Status

**Current stage:** OOP + Modular Architecture → Testing

The project is actively being developed.
