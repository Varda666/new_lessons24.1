from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from lms_service.models import Course, Lesson, Payment
from users.models import User


class ModelCreateTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            user_role='moderator',
            email='test@mail.com',
            first_name='Name',
            last_name='Last',
            phone='8976',
            country='RF',
            password='test'
        )
        self.client.force_authenticate(user=self.user)
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
            pay_id=12344321,
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
                        "course": self.course.name,
                        "description": self.lesson.description,
                        "id": 1,
                        "img": None,
                        "link": self.lesson.link,
                        "name": self.lesson.name,
                        'user': self.lesson.user.email,
                    }
                ]
            }

        )

    def test_lesson_create(self):
        data = {'name': 'Урок анг. яз 2',
                'description': 'Знакомство с анг. языком',
                'link': 'https://ru.stackoverflow.com/questions/1388409/django',
                'course': 'Анг. язык для начинающих',
                'user': self.user
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
        response = self.client.get(
            reverse(
                'lms_service:lesson_update',
                kwargs={'pk': self.lesson.pk},
            ))
        data = {'name': 'Урок франц. яз 2',
                'description': 'Знакомство с франц. языком',
                'link': 'https://ru.stackoverflow.com/questions/1388409/django',
                'course': 'Анг. язык для начинающих'
                }
        self.client.post(
            reverse(
                'lms_service:lesson_update',
                kwargs={'pk': self.lesson.pk}
        ),
            data=data)
        dict_response = response.json()
        print('Наш ответ', dict_response)
        self.assertEquals(
            dict_response.get('name'),
            'Урок франц. яз 2'
        )

    def test_lesson_delete(self):
        response = self.client.delete(
            reverse('lms_service:lesson_delete', kwargs={'pk': self.lesson.pk})
        )
        self.assertEqual(response.status_code, 204)
        self.assertEquals(
            Lesson.objects.all().count(),
            1
        )