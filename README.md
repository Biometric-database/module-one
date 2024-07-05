# Government Workers Data Management System

This project is a Django-based web application designed to collect, manage, and maintain data. The system is developed for a local government institution and consists of two main phases: initial data collection and live data capture.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)
- [Contact](#contact)

## Project Overview

The Government Workers Data Management System is designed to collect detailed information on government workers in multiple categories including personal data, official information, institutions attended, leave records, transformations, postings and transfers, and association/union membership. The system also supports a live data capture phase for collecting photos, fingerprints, and signatures to ensure data integrity and eliminate duplicate entries.

## Features

- **Data Collection:** Forms for collecting detailed information in seven categories.
- **Live Data Capture:** Interface for capturing and updating photos, fingerprints, and signatures.
- **User Authentication and Authorization:** Secure login and role-based access control.
- **Data Integrity:** Checks to prevent duplicate data entries.
- **Responsive Design:** User-friendly templates for data entry and live capture.
- **Reporting:** Tools for generating reports on collected data.

## Technologies Used

- **Django:** Web framework
- **SQLite/PostgreSQL:** Database
- **HTML5/CSS3:** Front-end design
- **JavaScript:** Front-end interactivity
- **Bootstrap:** Responsive design framework

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/gov-workers-data-management.git
   cd gov-workers-data-management
   ```

2. **Set Up Virtual Environment:**
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows use `env\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Database:**
   ```bash
   python manage.py migrate
   ```

5. **Create Superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Server:**
   ```bash
   python manage.py runserver
   ```

## Usage

1. **Access the Admin Interface:**
   Visit `http://127.0.0.1:8000/admin` and log in with the superuser credentials.

2. **Add Workers' Data:**
   Use the admin interface or custom forms to add workers' personal data, official information, etc.

3. **Live Data Capture:**
   Set up live capture stations and update worker records with photos, fingerprints, and signatures.

## Project Structure

```
gov-workers-data-management/
├── manage.py
├── projectname/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── appname/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── requirements.txt
└── README.md
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact

For questions or inquiries, please contact [yourname@yourdomain.com](mailto:yourname@yourdomain.com).
