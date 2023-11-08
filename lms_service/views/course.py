from rest_framework.viewsets import ModelViewSet

from lms_service.models import Course
from lms_service.serializers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer