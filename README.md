# Enrollment System – Student Profile View (Django)

An admin page that lists every student in a class and shows each student's profile
(personal info and enrollment) when selected.
Admins can add, edit and remove students. A summary row above the list shows
students in view, officially enrolled and pending review.

## Run it

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python manage.py makemigrations students
python manage.py migrate
python manage.py seed_students   # optional sample data
python manage.py createsuperuser # staff account used to sign in
python manage.py runserver
```

Open http://127.0.0.1:8000/ and sign in with the superuser account.
Only staff users can open the pages.

## Layout

- `students/models.py` – Student
- `students/views.py` – list + profile, add/edit, remove
- `students/forms.py` – student form and guardian/grade formsets
- `students/templates/students/` – list, form, confirm-remove templates
- `students/static/students/style.css` – grayscale palette (#FAFAFA → #18181B)
