from rest_framework import serializers

from lms_service.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    # paid_lesson = serializers.PrimaryKeyRelatedField(required=False, read_only=True)

    class Meta:
        model = Lesson
        fields = "__all__"


