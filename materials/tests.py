from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from materials.models import Course, Topic, Lecture
from users.models import User


class CourseAPITestCase(APITestCase):
    """Тесты для Учебного курса"""

    def setUp(self):
        self.user = User.objects.create(email='course@user.com', password='123456', role='teacher')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            title='Эталонный курс', description='Эталонный курс для тестирования', owner=self.user)
        self.topic = Topic.objects.create(
            title='Эталонная тема', description='Эталонная тема для тестирования', course=self.course,
            owner=self.user)
        self.lecture = Lecture.objects.create(
            title="Эталонная лекция", description="Эталонная лекция для тестирования", topic=self.topic,
            owner=self.user)

    def test_course_create(self):
        """Юниттест создания курса"""
        db_create = {
            'title': 'Тестовый курс',
            'description': 'Тестовый курс для тестирования'
        }
        url = reverse('materials:course-list')
        create_response = self.client.post(url, db_create)
        print(f'лог: {create_response}, {create_response.json()}')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            Course.objects.filter(title='Тестовый курс').count(), 1
        )

    def test_courses_list_get(self):
        """Юниттест вывода списка курсов"""
        url = reverse('materials:course-list')
        get_list_response = self.client.get(url)
        print(f'лог: {get_list_response}, {get_list_response.json()}')
        self.assertEqual(get_list_response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            get_list_response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': self.course.pk, 'topics': {'topics_count': 1, 'topics_list': ['Эталонная тема']},
                 'title': 'Эталонный курс', 'description': 'Эталонный курс для тестирования',
                 'imagery': None, 'owner': self.user.pk}]}
        )

    def test_course_retrieve(self):
        """Юниттест вывода детализации курса"""
        url = reverse('materials:course-detail', args=(self.course.pk,))
        detail_response = self.client.get(url)
        print(f'лог: {detail_response.json()}')
        self.assertEqual(detail_response.status_code, status.HTTP_200_OK)
        self.assertEqual(detail_response.data['title'], 'Эталонный курс')

    def test_course_delete(self):
        """Юниттест удаления курса"""
        url = reverse('materials:course-detail', args=(self.course.pk,))
        del_response = self.client.delete(url)
        print(f'лог: {del_response}')
        self.assertEqual(del_response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(
            Course.objects.filter(title='Эталонный курс').count(), 0
        )

    def test_course_put(self):
        """Юниттест обновления курса через put"""
        db_put = {
            'title': 'Измененный курс',
            'description': 'Описание измененного курса',
            'course': self.course.pk
        }
        url = reverse('materials:course-detail', args=(self.course.pk,))
        put_response = self.client.put(url, db_put)
        print(f'лог: {put_response}')
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.data['title'], 'Измененный курс')

    def test_course_patch(self):
        """Юниттест обновления курса через patch"""
        db_patch = {
            'description': 'Описание еще раз измененного курса',
        }
        url = reverse('materials:course-detail', args=(self.course.pk,))
        patch_response = self.client.patch(url, db_patch)
        print(f'лог: {patch_response}')
        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(patch_response.data['description'], 'Описание еще раз измененного курса')


class TopicAPITestCase(APITestCase):
    """Тесты для Темы курса"""

    def setUp(self):
        self.user = User.objects.create(email='topic@user.com', password='654321', role='teacher')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            title='Эталонный курс', description='Эталонный курс для тестирования', owner=self.user)
        self.topic = Topic.objects.create(
            title='Эталонная тема', description='Эталонная тема для тестирования', course=self.course,
            owner=self.user)
        self.lecture = Lecture.objects.create(
            title="Эталонная лекция", description="Эталонная лекция для тестирования", topic=self.topic,
            owner=self.user)

    def test_topic_create(self):
        """Юниттест создания темы"""
        db_create = {
            'course': self.course.pk,
            'title': 'Тестовая тема',
            'description': 'Тестовая тема для тестирования',
        }
        url = reverse('materials:topic-list')
        create_response = self.client.post(url, db_create)
        print(f'лог: {create_response}, {create_response.json()}')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            Topic.objects.filter(title='Тестовая тема').count(), 1
        )

    def test_topics_list_get(self):
        """Юниттест вывода списка тем"""
        url = reverse('materials:topic-list')
        get_list_response = self.client.get(url)
        print(f'лог: {get_list_response}, {get_list_response.json()}')
        self.assertEqual(get_list_response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            get_list_response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': self.topic.pk, 'lectures': {'lectures_count': 1, 'lectures_list': ['Эталонная лекция']},
                 'course': self.course.pk, 'title': 'Эталонная тема',
                 'description': 'Эталонная тема для тестирования',
                 'imagery': None, 'owner': self.user.pk}]}
        )

    def test_topic_retrieve(self):
        """Юниттест вывода детализации темы"""
        url = reverse('materials:topic-detail', args=(self.topic.pk,))
        detail_response = self.client.get(url)
        print(f'лог: {detail_response}, {detail_response.json()}')
        self.assertEqual(detail_response.status_code, status.HTTP_200_OK)
        self.assertEqual(detail_response.data['title'], 'Эталонная тема')

    def test_topic_delete(self):
        """Юниттест удаления темы"""
        url = reverse('materials:topic-detail', args=(self.topic.pk,))
        del_response = self.client.delete(url)
        print(f'лог: {del_response}')
        self.assertEqual(del_response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(
            Topic.objects.filter(title='Эталонная тема').count(), 0
        )

    def test_topic_put(self):
        """Юниттест обновления темы через put"""
        db_put = {
            'course': self.course.pk,
            'title': 'Измененная тема',
            'description': 'Описание измененной темы',
            'topic': self.topic.pk
        }
        url = reverse('materials:topic-detail', args=(self.topic.pk,))
        put_response = self.client.put(url, db_put)
        print(f'лог: {put_response}')
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.data['title'], 'Измененная тема')

    def test_topic_patch(self):
        """Юниттест обновления темы через patch"""
        db_patch = {
            'description': 'Описание еще раз измененной темы',
        }
        url = reverse('materials:topic-detail', args=(self.topic.pk,))
        patch_response = self.client.patch(url, db_patch)
        print(f'лог: {patch_response}')
        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(patch_response.data['description'], 'Описание еще раз измененной темы')


class LectureAPITestCase(APITestCase):
    """Тесты для Лекции"""

    def setUp(self):
        self.user = User.objects.create(email='lecture@user.com', password='654321', role='teacher')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            title='Эталонный курс', description='Эталонный курс для тестирования', owner=self.user)
        self.topic = Topic.objects.create(
            title='Эталонная тема', description='Эталонная тема для тестирования', course=self.course,
            owner=self.user)
        self.lecture = Lecture.objects.create(
            title="Эталонная лекция", description="Эталонная лекция для тестирования", topic=self.topic,
            owner=self.user)

    def test_lecture_create(self):
        """Юниттест создания лекции"""
        db_create = {
            'title': 'Тестовая лекция',
            'description': 'Тестовая лекция для тестирования',
            'topic': self.topic.pk
        }
        create_response = self.client.post('/lecture/create/', db_create)
        print(f'лог: {create_response}, {create_response.json()}')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            Lecture.objects.filter(title='Тестовая лекция').count(), 1
        )

    def test_lecture_validator(self):
        """Юниттест проверки работы валидатора"""
        db_create = {
            'topic': self.topic.pk,
            'title': 'Тестовая лекция c видео',
            'description': 'Тестовая лекция для тестирования',
            'video': 'https://www.youtube.com/video/Fdf454sd'

        }
        create_response = self.client.post('/lecture/create/', db_create)
        print(f'лог: {create_response}, {create_response.json()}')
        self.assertEqual(create_response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(create_response.json()['non_field_errors'], ['Размещение видео с хостинга YOUTUBE запрещено!'])

    def test_lectures_list_get(self):
        """Юниттест вывода списка лекций"""
        get_list_response = self.client.get('/lectures_list/')
        print(f'лог: {get_list_response}, {get_list_response.json()}')
        self.assertEqual(get_list_response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            get_list_response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': self.lecture.pk, 'topic': self.topic.pk, 'title': 'Эталонная лекция',
                 'description': 'Эталонная лекция для тестирования', 'imagery': None, 'content': None,
                 'video': None,
                 'owner': self.user.pk}]}
        )

    def test_lecture_retrieve(self):
        """Юниттест вывода детализации лекции"""
        url = f'/lecture/retrieve/{self.lecture.pk}/'
        detail_response = self.client.get(url)
        print(f'лог: {detail_response}, {detail_response.json()}')
        self.assertEqual(detail_response.status_code, status.HTTP_200_OK)
        self.assertEqual(detail_response.data['title'], 'Эталонная лекция')

    def test_lecture_delete(self):
        """Юниттест уаделения лекции"""
        url = f'/lecture/destroy/{self.lecture.pk}/'
        del_response = self.client.delete(url)
        print(f'лог: {del_response}')
        self.assertEqual(del_response.status_code, status.HTTP_204_NO_CONTENT)

    def test_lecture_put(self):
        """Юниттест обновления лекции через put"""
        db_put = {
            'lecture': self.lecture.pk,
            'title': 'Измененная эталонная лекция',
            'description': 'Описание измененной эталонной лекции',
            'topic': self.topic.pk
        }
        url = f'/lecture/update/{self.lecture.pk}/'
        put_response = self.client.put(url, db_put)
        print(f'лог: {put_response}')
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.data['title'], 'Измененная эталонная лекция')

    def test_lecture_patch(self):
        """Юниттест обновления лекции через patch"""
        db_patch = {
            'title': 'Эталонная лекция с видео',
            'video': 'https://rutube.ru/channel/23492802/'
        }
        url = f'/lecture/update/{self.lecture.pk}/'
        patch_response = self.client.patch(url, db_patch)
        print(f'лог: {patch_response}')
        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(patch_response.data['title'], 'Эталонная лекция с видео')
        self.assertEqual(patch_response.data['video'], 'https://rutube.ru/channel/23492802/')