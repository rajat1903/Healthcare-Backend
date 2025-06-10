# Healthcare Management System Backend

A Django REST Framework backend for managing healthcare data, including patients, doctors, and their relationships.<br><br>

## API Documentation
> Link : https://documenter.getpostman.com/view/44498594/2sB2x5Frrk<br><br>

## Features

- JWT Authentication
- Patient Management
- Doctor Management
- Patient-Doctor Mapping
- RESTful API Design
- PostgreSQL Database<br><br>

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a .env file with the following variables:
```
DEBUG=True
SECRET_KEY=your-secret-key-here
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

4. Create PostgreSQL database:
```bash
createdb healthcare_db
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```
<br><br>


## API Endpoints

### Authentication
- POST /api/auth/register/ - Register new user
- POST /api/auth/login/ - Login and get JWT token

### Patients
- POST /api/patients/ - Create patient
- GET /api/patients/ - List patients
- GET /api/patients/<id>/ - Get patient details
- PUT /api/patients/<id>/ - Update patient
- DELETE /api/patients/<id>/ - Delete patient

### Doctors
- POST /api/doctors/ - Create doctor
- GET /api/doctors/ - List doctors
- GET /api/doctors/<id>/ - Get doctor details
- PUT /api/doctors/<id>/ - Update doctor
- DELETE /api/doctors/<id>/ - Delete doctor

### Patient-Doctor Mappings
- POST /api/mappings/ - Create mapping
- GET /api/mappings/ - List mappings
- GET /api/mappings/<patient_id>/ - Get patient's doctors
- DELETE /api/mappings/<id>/ - Delete mapping<br><br>

## Images

![image](https://github.com/user-attachments/assets/64325697-3860-45ff-b7bd-e2f3666ac9e5)

![image](https://github.com/user-attachments/assets/c4d4edd7-65d4-4013-9dd0-314da703bb14)

![image](https://github.com/user-attachments/assets/24f2801b-2420-428f-b503-85d3b0491489)


