from datetime import date

from django.core.management.base import BaseCommand

from students.models import Student

SAMP, DAHL = "Grade 10 - Sampaguita", "Grade 10 - Dahlia"

DATA = [
    ("2026-0141", "Maria Angelica", "Dela Cruz", "Female", date(2010, 3, 14),
     "Nagcarlan, Laguna", "Roman Catholic", "0917 555 0141",
     "Brgy. Poblacion, Nagcarlan, Laguna", "Enrolled", "Continuing", SAMP),
    ("2026-0142", "Joshua Miguel", "Reyes", "Male", date(2010, 7, 2),
     "San Pablo City, Laguna", "Iglesia ni Cristo", "0927 555 0142",
     "Brgy. Bambang, Nagcarlan, Laguna", "Enrolled", "Continuing", SAMP),
    ("2026-0143", "Kyla Denise", "Santos", "Female", date(2010, 1, 22),
     "Calamba City, Laguna", "Roman Catholic", "0905 555 0143",
     "Brgy. Sulsuguin, Nagcarlan, Laguna", "Pending", "Transferee", SAMP),
    ("2026-0144", "Paolo Gabriel", "Villanueva", "Male", date(2009, 9, 9),
     "Lucban, Quezon", "Roman Catholic", "0998 555 0144",
     "Brgy. Lawaguin, Nagcarlan, Laguna", "Enrolled", "Continuing", SAMP),
    ("2026-0145", "Samantha Rose", "Aquino", "Female", date(2010, 5, 30),
     "Liliw, Laguna", "Born Again Christian", "0919 555 0145",
     "Brgy. Oples, Liliw, Laguna", "Enrolled", "Continuing", DAHL),
    ("2026-0146", "Carlo Antonio", "Mendoza", "Male", date(2009, 11, 11),
     "Santa Cruz, Laguna", "Roman Catholic", "0935 555 0146",
     "Brgy. Silangan, Santa Cruz, Laguna", "Withdrawn", "Continuing", DAHL),
    ("2026-0147", "Bea Nicole", "Ramos", "Female", date(2010, 12, 5),
     "Nagcarlan, Laguna", "Roman Catholic", "0916 555 0147",
     "Brgy. Taytay, Nagcarlan, Laguna", "Pending", "Late enrollee", SAMP),
]


class Command(BaseCommand):
    help = "Load sample students (skips any student ID that already exists)."

    def handle(self, *args, **options):
        created = 0
        for (sid, first, last, sex, dob, pob, rel, phone, addr,
             status, etype, section) in DATA:
            if Student.objects.filter(student_id=sid).exists():
                continue
            Student.objects.create(
                student_id=sid,
                first_name=first,
                last_name=last,
                sex=sex,
                date_of_birth=dob,
                place_of_birth=pob,
                religion=rel,
                phone=phone,
                address=addr,
                status=status,
                enrollment_type=etype,
                section=section,
                email=f"{first.split()[0].lower()}.{last.lower()}@school.example",
            )
            created += 1
        self.stdout.write(self.style.SUCCESS(f"Added {created} sample students."))
