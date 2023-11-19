from rest_framework import serializers

from lms_service.models import Course
from lms_service.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    # paid_course = serializers.PrimaryKeyRelatedField(required=False)
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(read_only=True)


    def get_lessons_count(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = "__all__"
