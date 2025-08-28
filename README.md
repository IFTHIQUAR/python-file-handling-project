File Management System (Python Project)
🔹 Project Description

This is a command-line File Management System built in Python.
It allows users to perform basic file operations such as:

Create new files

Read and display file contents

Write new data (overwrite)

Update data (append to existing files)

Delete files safely

Display all available files in the current directory

The project mimics how an operating system’s file manager works, but in a simplified, menu-driven Python application.


Why This Project?

I built this project to practice:

File handling in Python (open, read, write, append modes)

Using the os module for system-level file operations

Writing an interactive, menu-driven program

Learning exception handling (try-except) to make the program more reliable

This project helps me understand real-world file operations and is a strong exercise for strengthening Python fundamentals.


Key Challenges

Handling existing files during creation – Used "x" mode to avoid overwriting files accidentally.

Reading and updating missing files – Added FileNotFoundError checks.

Ensuring data safety – Differentiated between Write (w) which overwrites and Update (a) which appends.

Making it user-friendly – Implemented a menu loop (while True) for repeated operations.

Directory listing – Used os.listdir() to dynamically show all files in the current folder.


How This Project Can Be Used

As a mini file manager directly in the terminal.

For practicing Python file handling & exception handling.

To demonstrate CRUD operations on files.
