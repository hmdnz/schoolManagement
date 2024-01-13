# students/views.py
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
from django.shortcuts import render, get_object_or_404

from .forms import StudentUpdateForm  # Create this form in the next step

from django.views import View
from django.shortcuts import render, redirect


class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        form = StudentUpdateForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            # Redirect to the student detail page or any other page after successful update
    else:
        form = StudentUpdateForm(instance=student)

    return render(request, "students.html", {"form": form, "student": student})


class StudentRegistrationView(View):
    def get(self, request):
        form = StudentUpdateForm()
        return render(request, "register.html", {"form": form})

    def post(self, request):
        form = StudentUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("success")
        return render(request, "register.html", {"form": form})
