import django_filters as filters
from .models import Employee


class EmployeeFilter(filters.FilterSet):
min_join_date = filters.DateFilter(field_name="date_of_joining", lookup_expr="gte")
max_join_date = filters.DateFilter(field_name="date_of_joining", lookup_expr="lte")
department = filters.NumberFilter(field_name="department__id")


class Meta:
model = Employee
fields = ["department", "min_join_date", "max_join_date"]