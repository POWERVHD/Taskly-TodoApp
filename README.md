# [**📋Taskly-TodoApp**](https://taskly-deployment.onrender.com)
![image](https://github.com/user-attachments/assets/25a7430c-736b-4c65-91be-77ba5bf3ae01)

Taskly is a simple and efficient task management web application that helps users organize and track their daily tasks. With a clean user interface and intuitive functionality, Taskly makes managing to-do lists seamless and productive.
[🚀 Live Site](https://taskly-deployment.onrender.com)


## Features

✅ User Authentication (Signup & Login)\
✅ Add, Edit, and Delete Tasks\
✅ Responsive UI with Smooth Design\
✅ Secure CSRF-Protected Forms\
✅ Persistent Task Storage in Database

## Tech Stack

- **Frontend:** HTML, CSS 
- **Backend:** Django (Python)
- **Database:** SQLite (default), PostgreSQL (optional)
- **JavaScript:** Dynamic interactions
- **Version Control:** Git & GitHub

## Installation Guide

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.13.1
- pip (Python package manager)
- Git

### Steps to Set Up the Project

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/POWERVHD/Taskly--Todo-App
   cd taskly-todo
   ```

2. **Create a Virtual Environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate  # For Windows
   ```

3. **Install Dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Run Migrations:**

   ```sh
   python clear_sessions.py
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser (Optional - For Admin Panel Access):**

   ```sh
   python manage.py createsuperuser
   ```

6. **Run the Development Server:**

   ```sh
   python clear_sessions.py
   python manage.py runserver
   ```

7. **Access the App in Your Browser:**

   ```
   http://127.0.0.1:8000/
   ```



## License

This project is licensed under the **MIT License**.

## Contact

For any issues or feature requests, feel free to open an issue or contact:

- 📧 Email: [Kshitijprasad6@gmail.com](mailto\:Kshitijprasad6@gmail.com)
- 🐙 GitHub: [POWERVHD](https://github.com/POWERVHD)

Happy Tasking! ✅

