from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User


class UserAPITestCase(APITestCase):
    """Тесты для Пользователя"""

    def setUp(self):
        Group.objects.get_or_create(name='teacher')
        Group.objects.get_or_create(name='student')

    def test_user_student_create(self):
        """Юниттест создания пользователя с ролью student"""
        db_create = {
            'email': 'student1@user.com',
            'password': '654321',
            'role': 'student'
        }
        url = f'/user/create/'
        create_response = self.client.post(url, db_create)
        print(f'лог: {create_response}, {create_response.json()}')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 1)
        self.assertEqual(create_response.json().get("email"), 'student1@user.com')
        # проверка включения в группу student
        user_id = create_response.json().get("id")
        user = User.objects.get(pk=user_id)
        self.assertEqual(user.groups.filter(name='student').exists(), True)

    def test_user_teacher_create(self):
        """Юниттест создания пользователя с ролью teacher"""
        db_create = {
            'email': 'teacher1@user.com',
            'password': '123456',
            'role': 'teacher'
        }
        url = f'/user/create/'
        create_response = self.client.post(url, db_create)
        print(f'лог: {create_response}, {create_response.json()}')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 1)
        self.assertEqual(create_response.json().get("email"), 'teacher1@user.com')
        # проверка включения в группу teacher
        user_id = create_response.json().get("id")
        user = User.objects.get(pk=user_id)
        self.assertEqual(user.groups.filter(name='teacher').exists(), True)