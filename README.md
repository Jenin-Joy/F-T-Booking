# RESTO360 - Restaurant Management System

RESTO360 is a comprehensive restaurant management system built with Django, designed to streamline restaurant operations with multiple user roles and features.

## Features

### Customer Features
- User registration and authentication
- Menu browsing with detailed food items
- Table reservations
- Food ordering and cart management
- Online payment processing
- Feedback submission
- Complaint management
- Job vacancy viewing
- Profile management

### Admin Features
- Dashboard for restaurant management
- Category and subcategory management
- Food item management
- Staff management
- Table management
- Job listing management
- Order tracking
- User management

### Manager Features
- Order management
- Staff supervision
- Profile management
- Restaurant analytics

### Staff Features
- Order processing
- Profile management
- Task management

## Technology Stack

- **Backend Framework:** Django 5.1.3
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** Django ORM
- **Additional Libraries:** 
  - mathfilters
  - Font Awesome
  - Bootstrap Icons
  - jQuery UI

## Installation

1. Clone the repository
```bash
git clone [repository-url]
```

2. Create and activate virtual environment
```bash
python -m venv MainEnv
source MainEnv/bin/activate  # On Windows: MainEnv\Scripts\activate
```

3. Install dependencies
```bash
pip install django mathfilters
```

4. Apply migrations
```bash
python manage.py migrate
```

5. Run the development server
```bash
python manage.py runserver
```

## Project Structure

```
RESTO360/
├── Admin/          # Admin module
├── Guest/          # Guest/Public module
├── User/           # Customer module
├── Manager/        # Manager module
├── Staff/          # Staff module
├── MyPro/          # Project configuration
└── static/         # Static files
```

## User Roles

1. **Guest** - Unregistered users who can view the menu and register
2. **User** - Registered customers who can place orders and make reservations
3. **Staff** - Restaurant staff who handle orders and customer service
4. **Manager** - Restaurant managers with enhanced administrative capabilities
5. **Admin** - System administrators with full control over the platform

## Contributing

This project is part of a restaurant management solution. For major changes, please open an issue first to discuss what you would like to change.

## License

This project uses the HTML Codex Bootstrap Restaurant Template under their license terms. See `Guest/static/Main/READ-ME.txt` for more details.

## Acknowledgments

- Bootstrap Restaurant Template by HTML Codex
- Django Framework
- Bootstrap Framework
- Font Awesome Icons