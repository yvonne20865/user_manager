# User Manager Django Project

This is a Django project with custom user account functionality, including:
- User registration
- Email verification (console backend for development)
- Profile management
- Admin features

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
3. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Email
- By default, emails are printed to the console for development.
- To use SMTP, update the email settings in `user_manager/settings.py`.

## GitHub
- Project is hosted at: https://github.com/yvonne20865/user-manager

