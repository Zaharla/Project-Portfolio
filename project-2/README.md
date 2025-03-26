# School Library Database System

## Project Overview
This project is a relational database system designed to manage a school's library records efficiently. It allows tracking of books, students, borrowing history, and donations for events like World Book Day.

## Features
- **Book Management**: Stores book details including title, author, genre, and publication year.
- **Student Records**: Keeps track of students borrowing books.
- **Event Donations**: Tracks books donated for special events.

## Database Schema
The database consists of the following tables:

### Books Table
| Column         | Data Type | Description                    |
|--------------|-----------|--------------------------------|
| book_id       | INT (PK)  | Unique identifier for books   |
| title         | VARCHAR   | Book title                    |
| author        | VARCHAR   | Book author                   |
| genre         | VARCHAR   | Genre of the book             |
| published_year| INT       | Year the book was published   |
| event_donation | BOOLEAN  | If donated for an event       |

### Students Table
| Column        | Data Type | Description                     |
|--------------|-----------|---------------------------------|
| student_id   | INT (PK)  | Unique identifier for students |
| name         | VARCHAR   | Student's full name            |
| email        | VARCHAR   | Student's email address        |

### BorrowedBooks Table
| Column        | Data Type | Description                     |
|--------------|-----------|---------------------------------|
| borrow_id    | INT (PK)  | Unique transaction ID          |
| student_id   | INT (FK)  | References Students table      |
| book_id      | INT (FK)  | References Books table         |
| borrow_date  | DATE      | Date book was borrowed         |
| return_date  | DATE      | Date book was returned         |

## Technologies Used
- **MySQL** for database management
- **PyCharm** as the development environment

## Getting Started
1. Install MySQL and set up the database.
2. Run the provided SQL script to create tables.
3. Use MySQL Workbench or a Python script to interact with the database.

## Future Enhancements
- Implement a web interface for user interaction.
- Automate overdue book notifications.
- Add an admin panel for managing records.

---



