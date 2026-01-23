from rest_framework import viewsets

from .models import Course
from .serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.order_by("id")
    serializer_class = CourseSerializer
