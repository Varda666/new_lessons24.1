from rest_framework.viewsets import ModelViewSet

from lms_service.models import Course
from lms_service.permissions import IsModerator, IsOwner
from lms_service.serializers.course import CourseSerializer
from rest_framework.permissions import IsAuthenticated

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsModerator, IsOwner]