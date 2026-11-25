from urllib.parse import urlencode

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.db import transaction
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import StudentForm
from .models import Student

TABS = [
    ("personal", "Personal info"),
    ("enrollment", "Enrollment & billing"),
]


def _detail(pk):
    return Student.objects.filter(pk=pk).first()


@staff_member_required
def student_list(request):
    status = request.GET.get("status", "")
    section = request.GET.get("section", "")
    q = request.GET.get("q", "").strip()

    def query(**override):
        params = {"status": status, "section": section, "q": q, **override}
        return urlencode({k: v for k, v in params.items() if v})

    base = Student.objects.all()
    if section:
        base = base.filter(section=section)
    if q:
        base = base.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q) | Q(student_id__icontains=q))
    students = list(base.filter(status=status) if status in Student.Status.values else base)

    stats = {
        "in_view": len(students),
        "enrolled": base.filter(status=Student.Status.ENROLLED).count(),
        "pending": base.filter(status=Student.Status.PENDING).count(),
    }

    pk = request.GET.get("student", "")
    selected = _detail(pk) if pk.isdigit() else None
    viewing = selected is not None
    if not selected and students:
        selected = _detail(students[0].pk)

    tab = request.GET.get("tab", "personal")
    if tab not in dict(TABS):
        tab = "personal"

    chips = [(label, query(status=value), status == value)
             for label, value in [("All", ""), ("Enrolled", "Enrolled"),
                                  ("Pending", "Pending"), ("Withdrawn", "Withdrawn")]]
    return render(request, "students/list.html", {
        "students": students, "selected": selected, "viewing": viewing, "tab": tab, "tabs": TABS,
        "stats": stats, "chips": chips, "keep": query(), "q": q, "status": status, "section": section,
        "sections": Student.objects.order_by("section").values_list("section", flat=True).distinct(),
        "total": Student.objects.count(),
    })


def _next_student_id():
    n = Student.objects.count() + 1
    while Student.objects.filter(student_id=f"2026-{n:04d}").exists():
        n += 1
    return f"2026-{n:04d}"


@staff_member_required
def student_edit(request, pk=None):
    instance = get_object_or_404(Student, pk=pk) if pk else None

    if request.method == "POST":
        form = StudentForm(request.POST, instance=instance)
        if form.is_valid():
            with transaction.atomic():
                student = form.save()
            messages.success(request, f"{student.full_name} was {'updated' if instance else 'added'}.")
            return redirect(f"/?student={student.pk}")
    else:
        form = StudentForm(instance=instance, initial=None if instance else {"student_id": _next_student_id()})

    return render(request, "students/form.html", {
        "form": form, "student": instance,
    })


@staff_member_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        name = student.full_name
        student.delete()
        messages.success(request, f"{name} was removed from the class.")
        return redirect("student_list")
    return render(request, "students/confirm_delete.html", {"student": student})
