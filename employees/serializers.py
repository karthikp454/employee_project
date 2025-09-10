from rest_framework import serializers
from .models import Department, Employee


class DepartmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Department
		fields = ["id", "name"]


class EmployeeSerializer(serializers.ModelSerializer):
	department = DepartmentSerializer(read_only=True)
	department_id = serializers.PrimaryKeyRelatedField(
		queryset=Department.objects.all(), source="department", write_only=True
	)

	class Meta:
		model = Employee
		fields = [
			"id",
			"first_name",
			"last_name",
			"email",
			"phone",
			"address",
			"date_of_joining",
			"department",
			"department_id",
		]