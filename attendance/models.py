from django.db import models
from employees.models import Employee


class Attendance(models.Model):
PRESENT = "present"
ABSENT = "absent"
LATE = "late"
STATUS_CHOICES = [
(PRESENT, "Present"),
(ABSENT, "Absent"),
(LATE, "Late"),
]


employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="attendance")
date = models.DateField()
status = models.CharField(max_length=10, choices=STATUS_CHOICES)


class Meta:
unique_together = ("employee", "date")
ordering = ["-date"]


class Performance(models.Model):
employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="reviews")
rating = models.IntegerField() # 1 to 5
review_date = models.DateField()


class Meta:
ordering = ["-review_date"]