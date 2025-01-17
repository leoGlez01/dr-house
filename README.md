# Medical Consultation Appointment Booking System

This Django project is designed to facilitate appointment booking for medical consultations. It includes user authentication features such as login, registration, and logout.

## Features

- User registration and authentication
- Appointment booking system
- User-friendly interface for managing appointments

## Project Structure

- **appointments/**: Contains the main application for managing appointments.
  - **migrations/**: Database migrations for the appointments app.
  - **static/**: Static files such as CSS.
  - **templates/**: HTML templates for rendering views.
  - **admin.py**: Admin interface configuration.
  - **models.py**: Database models for the application.
  - **views.py**: Logic for handling requests and responses.
  - **urls.py**: URL routing for the appointments app.

- **medical_consultation/**: Project configuration files.
  - **settings.py**: Project settings and configurations.
  - **urls.py**: Main URL routing for the project.
  - **wsgi.py**: WSGI configuration for deployment.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd medical_consultation
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Access the application at `http://127.0.0.1:8000/`.
- Register a new account or log in to book appointments.

## License

This project is licensed under the MIT License.