# Library Models Crud 

This is a Django-based project that implements a library management system with features like managing books, authors, and publishers using Django REST Framework (DRF). The project provides API endpoints for interacting with the resources.

## Features

- **Publisher Management**: Manage publishers with fields like name, address, and email.
- **Author Management**: Manage authors with fields like name and biography.
- **Book Management**: Manage books with title, publication date, genre, and relations to authors and publishers.
- **CRUD Operations**: Full support for Create, Read, Update, and Delete (CRUD) operations via a RESTful API.
- **Authentication**: (Optional) Basic authentication for accessing the API, which can be customized.

## Installation Instructions

Follow these steps to set up the project locally.

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/library_project.git
cd library_project
```
## API Endpoints
This project exposes several API endpoints for managing the library's resources (publishers, authors, books).

### Publishers
1) GET /api/publishers/: List all publishers.
2) POST /api/publishers/: Create a new publisher.
3) PUT /api/publishers/{id}/: Update an existing publisher.
4) DELETE /api/publishers/{id}/: Delete a publisher.

### Authors
1) GET /api/authors/: List all authors.
2) POST /api/authors/: Create a new author.
3) PUT /api/authors/{id}/: Update an existing author.
4) DELETE /api/authors/{id}/: Delete an author.

### Books
1) GET /api/books/: List all books.
2) POST /api/books/: Create a new book.
3) PUT /api/books/{id}/: Update an existing book.
4) DELETE /api/books/{id}/: Delete a book.