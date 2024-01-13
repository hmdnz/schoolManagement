# students/urls.py
from django.urls import path
from .views import StudentListCreateView, StudentDetailView, StudentRegistrationView
from .views import update_student

urlpatterns = [
    path("students/", StudentListCreateView.as_view(), name="student-list-create"),
    path("students/<int:pk>/", StudentDetailView.as_view(), name="student-detail"),
    path("students/<int:pk>/update/", update_student, name="update-student"),
    path(
        "student-registeration/",
        StudentRegistrationView.as_view(),
        name="student-list-create",
    ),
    # Add more URL patterns for other views if needed
]
