from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms_service.models import Course, Lesson, Payment
from users.models import User


class ModelCreateTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='varda@inbox.ru',
            first_name='Oksana',
            last_name='Ivanova',
            phone='79118245323',
            country='RF'

        )
        self.course = Course.objects.create(
            name='Анг. язык для начинающих',
            description='Получение уровня А',
            lessons_count=2,
            user=self.user,
        )

        self.lesson = Lesson.objects.create(
            name='Урок анг. яз 1',
            description='Знакомство с анг. языком',
            link='https://www.youtube.com/123',
            course=self.course,
            user=self.user,

        )

        self.payment = Payment.objects.create(
            user=self.user,
            pay_date='2022-11-21',
            paid_course=self.course,
            paid_lesson=self.lesson,
            payment_amount=3000,
            payment_method='transfer',
        )

    def test_get_list(self):
        response = self.client.get(
            reverse('lms_service:lesson_list')
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "name": self.lesson.name,
                        "description": self.lesson.description,
                        "link": self.lesson.link,
                        'course': self.lesson.course,
                        'user': self.lesson.user,
                    }
                ]
            }

        )

    def test_lesson_create(self):
        data = {'name': 'Урок анг. яз 2',
                'description': 'Знакомство с анг. языком',
                'link': 'https://ru.stackoverflow.com/questions/1388409/django',
                'course': 'Анг. язык для начинающих'
                }
        response = self.client.post(
            reverse('lms_service:lesson_create'),
            data=data
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            Lesson.objects.all().count(),
            2
        )

    def test_lesson_update(self):
        response = self.client.get('/update/1/')
        response = self.client.put(
            reverse('lms_service:lesson_update'),
            data=data
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            Lesson.objects.all().count(),
            2
        )

    def test_lesson_delete(self):
        response = self.client.delete('/delete/1/')
        self.assertEqual(response.status_code, 204)

        self.assertEquals(
            Lesson.objects.all().count(),
            1
        )