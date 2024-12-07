# CODSOFT PYTHON PROGRAMMING
These include beginner level projects completed during internship at Codsoft.
TASK 1 
This is a basic graphical user interface (GUI) calculator built using Python's Tkinter library. The application supports standard arithmetic operations such as addition, subtraction, multiplication, and division.
Features:
Basic Operations: Add, subtract, multiply, and divide.
Clear Function: Clears the current expression.
Result Memory: Stores the previous result and allows you to continue calculations.
Error Handling: Handles division by zero and other errors with a user-friendly error message.
Key Components:
Tkinter GUI: The interface includes a text field for the expression and buttons for digits, operators, and functions.
Expression Parsing: The calculator evaluates the mathematical expression entered by the user using Python's eval() function.
Custom Operator Handling: The multiplication operator is handled as x on the UI, but internally converted to * for evaluation.

TASK 2
This is a simple contact book application built using Python's Tkinter library. The application allows users to manage their contacts by adding, updating, viewing, and deleting contact information such as name and phone number. It provides a user-friendly interface to easily manage and organize contacts.
Features:
Add Contact: Add new contacts with a name and phone number.
Update Contact: Update existing contact details.
Delete Contact: Remove contacts from the list.
View Contact: View the details of a selected contact.
Contact List: Display a list of all added contacts in a scrollable listbox.
Window Management: Includes options to minimize, close, and toggle the window size (maximize/minimize).
Error Handling: Provides error messages for missing information or no contact selected.
Key Components:
Tkinter GUI: The interface includes fields for entering contact information and buttons for managing the contact list.
Contact List: Contacts are stored in a list and displayed in a scrollable listbox.
Window Actions: Ability to minimize, close, and toggle the window size for user convenience.

TASK 3
This is a simple Password Generator application built using Python's Tkinter library for the GUI and SQLite for storing generated passwords. The application allows users to create strong, random passwords of specified lengths, store them along with a username, and retrieve them later.
Features:
Generate Strong Passwords: Generates random passwords using uppercase, lowercase letters, numbers, and special characters.
Username and Password Storage: Saves the generated password along with a username in an SQLite database for future reference.
Password Length Validation: Ensures that the generated password is at least 5 characters long.
User Input Validation: Checks that the username is a string and not empty.
Clear Input Fields: Resets the input fields to their initial state after generating or saving a password.
Key Components:
Tkinter GUI: The interface includes fields for entering a username, specifying the password length, and displaying the generated password.
SQLite Database: A simple SQLite database (users.db) is used to store the usernames and their corresponding generated passwords.
Password Generation: The password is generated using a mix of upper and lowercase letters, special characters, and numbers.
Buttons and Actions: The interface provides buttons for generating passwords, accepting the entered details, and clearing the input fields.

TASK 4
This is a To-Do List application built using Python's Tkinter library for the graphical user interface and SQLite for persistent task storage. The application allows users to add, delete, and clear tasks, with all tasks saved in an SQLite database. The tasks are displayed in a listbox and can be selected for deletion.
Features:
Add Tasks: Allows the user to add tasks to the list.
Delete Tasks: Users can delete a single selected task or clear all tasks from the list.
Persistent Storage: Tasks are saved in a local SQLite database (listOfTasks.db), so they persist between sessions.
Error Handling: Provides feedback if no task is selected for deletion.
Clear All: Clears all tasks with confirmation.
User-Friendly Interface: Simple interface to add, delete, and manage tasks.
Key Components:
Tkinter GUI: The interface includes an input field for adding tasks and a listbox to display tasks.
SQLite Database: A simple SQLite database (listOfTasks.db) is used to store tasks. If the database does not exist, it is created automatically.
Listbox for Task Display: Tasks are displayed in a scrollable list, allowing easy selection and deletion.
Task Management: Users can add, delete, or clear tasks, and the app will update both the GUI and the database.
