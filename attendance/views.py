from rest_framework import viewsets, permissions
from django.db import models
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Attendance, Performance
from .serializers import AttendanceSerializer, PerformanceSerializer
from .filters import AttendanceFilter, PerformanceFilter


class AttendanceViewSet(viewsets.ModelViewSet):
	queryset = Attendance.objects.select_related("employee").all()
	serializer_class = AttendanceSerializer
	permission_classes = [permissions.IsAuthenticated]
	filterset_class = AttendanceFilter
	ordering_fields = ["date", "id"]

	@action(detail=False, methods=["get"], permission_classes=[permissions.IsAuthenticated])
	def monthly_overview(self, request):
		qs = Attendance.objects.values("date__year", "date__month", "status").annotate(count=models.Count("id"))
		return Response(list(qs))


class PerformanceViewSet(viewsets.ModelViewSet):
	queryset = Performance.objects.select_related("employee").all()
	serializer_class = PerformanceSerializer
	permission_classes = [permissions.IsAuthenticated]
	filterset_class = PerformanceFilter
	ordering_fields = ["review_date", "rating", "id"]