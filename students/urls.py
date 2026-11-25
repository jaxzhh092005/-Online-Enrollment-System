from django.urls import path

from . import views

urlpatterns = [
    path("", views.student_list, name="student_list"),
    path("students/add/", views.student_edit, name="student_add"),
    path("students/<int:pk>/edit/", views.student_edit, name="student_edit"),
    path("students/<int:pk>/remove/", views.student_delete, name="student_delete"),
]
