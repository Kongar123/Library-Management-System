# Library Management System

#### Video Demo: https://youtu.be/okuSeDRTvrI

#### Description:

The Library Management System is a Python-based application designed to streamline the management of library resources. This system allows users to efficiently manage books, members, and transactions, providing a comprehensive solution for small to medium-sized libraries. The application operates through a command-line interface, making it accessible and straightforward for users to interact with.

### Features:

- **Add Book**: Users can add new books to the library's catalog by providing the ISBN, title, author, and number of copies available. The system ensures that each book has a unique ISBN and validates the format of the ISBN to maintain data integrity.
- **Search Books**: The search functionality allows users to find books based on ISBN, title, or author. This feature helps in quickly locating specific books within the library's collection.
- **Add Member**: New library members can be added with a unique member ID and name. The system checks for duplicate member IDs to prevent data entry errors.
- **Issue Book**: Books can be issued to members, reducing the available copies in the library's inventory. The system updates both the book's copy count and the member's borrowed book list. It also logs the transaction for record-keeping.
- **Return Book**: When books are returned, the system updates the available copies and removes the book from the member’s borrowed list. It also logs the return transaction.
- **View Transactions**: Users can view all transactions, including book issues and returns, displayed in a tabular format. This feature helps track the history of library transactions.
- **View Books**: The system provides a list of all books currently in the library, displaying details such as ISBN, title, author, and number of available copies.
- **View Members**: A list of all library members along with their borrowed books is available for review.

### Files and Functionality:

- **`project.py`**: This is the main script file containing the core functionality of the Library Management System. It includes functions for adding books and members, issuing and returning books, and viewing transactions, books, and members. It also handles the loading and saving of data in JSON format and manages the command-line interface.
- **`README.md`**: This file provides an overview of the project, its features, and usage instructions. It helps users understand the purpose of the project and how to interact with it.

### Design Choices:

- **Command-Line Interface**: The decision to use a command-line interface was made to keep the project simple and focused on core functionalities without the complexity of a graphical user interface. This approach also makes it easier to test and deploy the system.
- **Data Storage**: JSON format was chosen for data storage due to its simplicity and ease of use. It provides a lightweight method for saving and loading data, ensuring persistence across sessions.
- **External Libraries**: The use of `prettytable` for tabular data presentation enhances readability. `pyfiglet` adds a visual touch with ASCII art for the system’s title. `cowsay` was included to provide playful feedback messages, adding a touch of fun to the user experience.
- **ISBN Validation**: The system includes validation for ISBNs to ensure that only correctly formatted identifiers are used. This helps maintain the accuracy and consistency of book records.
- **Unit Testing**:`pytest`: Unit tests have been implemented using pytest to validate the core functions of the Library Management System. These tests cover adding books and members, issuing and returning books, and other critical operations. Running these tests helps ensure that the system behaves as expected and can handle various edge cases.

### Future Improvements:

- **User Authentication**: Adding user authentication could enhance security and manage access levels for different types of users.
- **Graphical User Interface**: Transitioning to a graphical user interface could make the system more user-friendly and accessible to a broader audience.
- **Enhanced Search Functionality**: Implementing more advanced search features, such as filtering by publication year or genre, could improve the user experience.

This Library Management System provides a solid foundation for managing library operations efficiently. The design choices were made with simplicity and functionality in mind, ensuring that the system meets the needs of its users while remaining easy to maintain and extend.
