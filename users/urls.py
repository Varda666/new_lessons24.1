from django.urls import path

from lms_service.views.lesson import LessonListView

urlpatterns = [
    path('', LessonListView.as_view(), name='lesson_list'),
    ]