from django.urls import path
from rest_framework import routers
from django.contrib import admin

from lms_service.views.lesson import *
from lms_service.views.course import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LessonListView.as_view(), name='lesson_list'),
    path('<int:pk>/', LessonRetrieveView.as_view(), name='lesson_detail'),
    path('update/<int:pk>/', LessonUpdateView.as_view(), name='lesson_update'),
    path('create/', LessonCreateView.as_view(), name='lesson_create'),
    path('delete/<int:pk>/', LessonDestroyView.as_view(), name='lesson_delete'),
    ]

router = routers.SimpleRouter()
router.register('course', CourseViewSet)
urlpatterns += router.urls
