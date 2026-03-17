# 🏎️ F1 Race Hub

F1 Race Hub is a Django web application for managing Formula 1 drivers, teams, and races.
The project demonstrates core Django concepts including models, forms, views, templates, and database relationships.

---

## 🚀 Features

* Manage **Drivers, Teams, and Races**
* Full CRUD functionality for:

  * Drivers
  * Teams
* Add drivers to races and track race results
* Filter and sort drivers (Driver Standings page)
* Custom template filter (`ordinal`) for race positions
* Read-only fields in forms (driver name in edit form)
* Responsive UI using Bootstrap
* Custom 404 error page

---

## 🧱 Project Structure

The project is organized into three main Django apps:

### 📦 drivers

* Handles driver data
* CRUD operations for drivers
* Driver standings (filtering & sorting)

### 📦 teams

* Manages Formula 1 teams
* Displays team details and assigned drivers

### 📦 races

* Manages races and race results
* Allows adding drivers to races
* Tracks position, points, and fastest lap

---

## 🗂️ Directory Overview

```
f1_race_hub/
│
├── f1_race_hub/        # Project configuration
│   ├── settings.py
│   ├── urls.py
│
├── drivers/            # Drivers app
├── teams/              # Teams app
├── races/              # Races app
│
├── templates/          # Global templates
│   ├── base.html
│   ├── 404.html
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🛠️ Technologies Used

* Python 3.x
* Django
* PostgreSQL
* Bootstrap 5

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/crbonev/f1_race_hub.git
cd f1_race_hub
```

---

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your_secret_key

DB_NAME=f1_race_hub_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

⚠️ The `.env` file is not included in the repository for security reasons.

---

### 5. Configure PostgreSQL

Make sure PostgreSQL is running and create a database:

```sql
CREATE DATABASE f1_race_hub_db;
```

---

### 6. Apply migrations

```bash
python manage.py migrate
```

---

### 7. Run the server

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

## 🧪 Application Functionality

### Drivers

* Create, edit, delete drivers
* View driver details
* Filter and sort drivers (standings)

### Teams

* Create, edit, delete teams
* View team details and drivers

### Races

* Create races
* Add drivers to races
* Track results (position, points, fastest lap)

---

## 🔐 Environment Variables

The application uses environment variables for sensitive configuration:

* `SECRET_KEY`
* `DB_NAME`
* `DB_USER`
* `DB_PASSWORD`
* `DB_HOST`
* `DB_PORT`

If not provided, default development values may be used.

---

## 👨‍💻 Author

Created by **Kristian Bonev**

---

## 📌 Notes

This project was developed as part of the Django Basics course at SoftUni and demonstrates understanding of basic Django architecture, clean code practices, and web development fundamentals.
