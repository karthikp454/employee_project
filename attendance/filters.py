import django_filters as filters
from .models import Attendance, Performance


class AttendanceFilter(filters.FilterSet):
start = filters.DateFilter(field_name="date", lookup_expr="gte")
end = filters.DateFilter(field_name="date", lookup_expr="lte")
status = filters.CharFilter(field_name="status")


class Meta:
model = Attendance
fields = ["employee", "status", "start", "end"]


class PerformanceFilter(filters.FilterSet):
min_rating = filters.NumberFilter(field_name="rating", lookup_expr="gte")
max_rating = filters.NumberFilter(field_name="rating", lookup_expr="lte")


class Meta:
model = Performance
fields = ["employee", "min_rating", "max_rating"]