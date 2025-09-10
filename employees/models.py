from django.db import models


class Department(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.name


class Employee(models.Model):
	first_name = models.CharField(max_length=80)
	last_name = models.CharField(max_length=80)
	email = models.EmailField(unique=True)
	phone = models.CharField(max_length=20, blank=True)
	address = models.CharField(max_length=255, blank=True)
	date_of_joining = models.DateField()
	department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name="employees")

	class Meta:
		ordering = ["last_name", "first_name"]

	def __str__(self):
		return f"{self.first_name} {self.last_name}"