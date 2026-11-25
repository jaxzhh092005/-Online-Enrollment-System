from django.db import models


class Student(models.Model):
    class Status(models.TextChoices):
        ENROLLED = "Enrolled", "Enrolled"
        PENDING = "Pending", "Pending"
        WITHDRAWN = "Withdrawn", "Withdrawn"

    class EnrollmentType(models.TextChoices):
        CONTINUING = "Continuing", "Continuing"
        TRANSFEREE = "Transferee", "Transferee"
        LATE = "Late enrollee", "Late enrollee"

    class Sex(models.TextChoices):
        FEMALE = "Female", "Female"
        MALE = "Male", "Male"

    # Personal info
    student_id = models.CharField("Student ID", max_length=20, unique=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    sex = models.CharField(max_length=10, choices=Sex.choices)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=120, blank=True)
    nationality = models.CharField(max_length=60, default="Filipino")
    religion = models.CharField(max_length=60, blank=True)
    languages = models.CharField("Languages spoken", max_length=120, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField("Mobile", max_length=30, blank=True)
    address = models.CharField("Home address", max_length=200, blank=True)

    # Enrollment
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.PENDING)
    enrollment_type = models.CharField(max_length=20, choices=EnrollmentType.choices,
                                       default=EnrollmentType.CONTINUING)
    section = models.CharField("Grade and section", max_length=80, default="Grade 10 – Sampaguita")
    school_year = models.CharField(max_length=20, default="2026–2027")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.full_name} ({self.student_id})"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def initials(self):
        return (self.first_name[:1] + self.last_name[:1]).upper()

