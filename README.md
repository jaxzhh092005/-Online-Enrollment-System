# Enrollment System – Student Profile View (Django)

A student system that lists every student in a class and shows each student's profile
(personal info and enrollment) when selected.
Users can add, edit and remove students without signing in. A summary row above the list shows
students in view, officially enrolled and pending review.

## Run it

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python manage.py makemigrations students
python manage.py migrate
python manage.py seed_students   # optional sample data
python manage.py runserver
```

Open http://127.0.0.1:8000/ to use the system directly. No admin account is required.
The student system is publicly accessible; anyone who can reach it can add, edit, or remove records.
Create a superuser only if you need to use Django's separate `/admin/` interface.

## Layout

- `students/models.py` – Student
- `students/views.py` – list + profile, add/edit, remove
- `students/forms.py` – student form and guardian/grade formsets
- `students/templates/students/` – list, form, confirm-remove templates
- `students/static/students/style.css` – grayscale palette (#FAFAFA → #18181B)
