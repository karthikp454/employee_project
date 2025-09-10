from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AttendanceViewSet, PerformanceViewSet


router = DefaultRouter()
router.register(r"records", AttendanceViewSet)
router.register(r"performance", PerformanceViewSet)


urlpatterns = [
path("", include(router.urls)),
]