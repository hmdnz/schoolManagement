# students/models.py
from django.db import models


class Student(models.Model):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"

    SEX_CHOICES = [
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other"),
    ]

    student_no = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, default=OTHER)
    dob = models.DateField()
    home_address = models.TextField()
    city = models.CharField(max_length=50)

    STATE_CHOICES = [
        ("KN", "Kano"),
        ("JI", "Jigawa"),
        ("AB", "Abia"),
        # ... (other state choices)
    ]
    state = models.CharField(max_length=50, choices=STATE_CHOICES)

    picture = models.ImageField(upload_to="student_pictures/", blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    special_needs = models.TextField(blank=True, null=True)
    emergency_no = models.CharField(max_length=15)

    CLASS_CHOICES = [
        ("preNursery", "PreNursery"),
        ("nurseryOne", "Nursery1"),
        ("nurseryTwo", "Nursery2"),
        # ... (other class choices)
    ]
    student_class = models.CharField(max_length=20, choices=CLASS_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
