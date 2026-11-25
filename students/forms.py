from django import forms
from .models import Student

GROUPS = [
    ("Student details", ["student_id", "first_name", "last_name", "sex", "date_of_birth",
                         "place_of_birth", "nationality", "religion", "languages"]),
    ("Contact", ["email", "phone", "address"]),
    ("Enrollment", ["status", "enrollment_type", "section", "school_year"]),
]


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ["created_at"]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
        }

    def grouped(self):
        return [(title, [self[name] for name in names]) for title, names in GROUPS]
