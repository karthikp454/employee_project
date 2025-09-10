from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer
from .filters import EmployeeFilter


class DepartmentViewSet(viewsets.ModelViewSet):
queryset = Department.objects.all()
serializer_class = DepartmentSerializer
permission_classes = [permissions.IsAuthenticated]
filterset_fields = ["name"]
search_fields = ["name"]
ordering_fields = ["name", "id"]


class EmployeeViewSet(viewsets.ModelViewSet):
queryset = Employee.objects.select_related("department").all()
serializer_class = EmployeeSerializer
permission_classes = [permissions.IsAuthenticated]
filterset_class = EmployeeFilter
search_fields = ["first_name", "last_name", "email"]
ordering_fields = ["last_name", "date_of_joining", "id"]


@action(detail=False, methods=["get"], permission_classes=[permissions.IsAuthenticated])
def per_department_counts(self, request):
data = (
Employee.objects.values("department__name")
.order_by("department__name")
.annotate(count=models.Count("id"))
)
return Response(list(data))