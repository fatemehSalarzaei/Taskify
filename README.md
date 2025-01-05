# Task Manager API

Task Manager API is a Django-based project designed to manage tasks, users, projects, notifications, and reports. This project leverages Django REST Framework (DRF) for API development and includes Swagger for API documentation.

## Features
- **Task Management**: Create, update, delete, and manage tasks.
- **User Management**: User authentication and profile management.
- **Project Organization**: Group tasks under projects.
- **Notifications**: Notify users about updates or events.
- **Reports**: Generate reports for tasks and projects.

## Requirements
- Python 3.8+
- Django 4.2+
- Django REST Framework
- drf-yasg (for Swagger UI)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/task-manager.git
   cd task-manager
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## API Documentation
Swagger UI is available at:
- [Swagger UI](http://127.0.0.1:8000/swagger/)
- [ReDoc UI](http://127.0.0.1:8000/redoc/)

## Future Improvements
- Add advanced filtering and searching capabilities.
- Implement analytics and reporting features.
- Enhance user roles and permissions.
- Add integration with external services (e.g., email, SMS).


## Contributing
Contributions are welcome! Please submit a pull request or open an issue to get started.

---
**Author**: Fatemeh Salarzaei
