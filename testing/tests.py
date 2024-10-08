from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from materials.models import Course, Topic
from testing.models import Test, Question, Answer
from users.models import User


class TestAPITestCase(APITestCase):
    """Тесты для Теста"""

    def setUp(self):
        self.user = User.objects.create(email='course@user.com', password='123456', role='teacher')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            title='Эталонный курс', description='Эталонный курс для тестирования', owner=self.user)
        self.topic = Topic.objects.create(
            title='Эталонная тема', description='Эталонная тема для тестирования', course=self.course,
            owner=self.user)
        self.test = Test.objects.create(
            description='Эталонный тест для эталонной темы', topic=self.topic)

    def test_test_create(self):
        """Юниттест создания теста"""
        db_create = {
            'description': 'Тестовый тест для тестирования',
            'topic': self.topic.pk
        }
        url = reverse('testing:test-list')
        create_response = self.client.post(url, db_create)
        print(f'лог: {create_response}, {create_response.json()}')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            Test.objects.filter(description='Тестовый тест для тестирования').count(), 1
        )

    def test_test_list_get(self):
        """Юниттест вывода списка тестов"""
        url = reverse('testing:test-list')
        get_list_response = self.client.get(url)
        print(f'лог: {get_list_response}, {get_list_response.json()}')
        self.assertEqual(get_list_response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            get_list_response.json(),
            {'count': 1, 'next': None, 'previous': None,
             'results': [
                 {'id': self.test.pk, 'description': 'Эталонный тест для эталонной темы', 'topic': self.topic.pk}]}
        )

    def test_test_retrieve(self):
        """Юниттест вывода детализации теста"""
        url = reverse('testing:test-detail', args=(self.test.pk,))
        detail_response = self.client.get(url)
        print(f'лог: {detail_response.json()}')
        self.assertEqual(detail_response.status_code, status.HTTP_200_OK)
        self.assertEqual(detail_response.data['description'], 'Эталонный тест для эталонной темы')

    def test_test_delete(self):
        """Юниттест удаления теста"""
        url = reverse('testing:test-detail', args=(self.test.pk,))
        del_response = self.client.delete(url)
        print(f'лог: {del_response}')
        self.assertEqual(del_response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(
            Course.objects.filter(description='Эталонный тест для эталонной темы').count(), 0
        )

    def test_test_put(self):
        """Юниттест обновления теста через put"""
        db_put = {
            'description': 'Описание измененного теста',
            'topic': self.topic.pk
        }
        url = reverse('testing:test-detail', args=(self.test.pk,))
        put_response = self.client.put(url, db_put)
        print(f'лог: {put_response}')
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.data['description'], 'Описание измененного теста')

    def test_course_patch(self):
        """Юниттест обновления теста через patch"""
        db_patch = {
            'description': 'Описание еще раз измененного теста',
        }
        url = reverse('testing:test-detail', args=(self.test.pk,))
        patch_response = self.client.patch(url, db_patch)
        print(f'лог: {patch_response}')
        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(patch_response.data['description'], 'Описание еще раз измененного теста')


class QuestionAPITestCase(APITestCase):
    """Тесты для Вопроса"""

    def setUp(self):
        self.user = User.objects.create(email='course@user.com', password='123456', role='teacher')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            title='Эталонный курс', description='Эталонный курс для тестирования', owner=self.user)
        self.topic = Topic.objects.create(
            title='Эталонная тема', description='Эталонная тема для тестирования', course=self.course,
            owner=self.user)
        self.test = Test.objects.create(
            description='Эталонный тест для эталонной темы', topic=self.topic)
        self.question = Question.objects.create(
            question='Эталонный вопрос для эталонного теста', test=self.test)

    def test_question_create(self):
        """Юниттест создания вопроса"""
        db_create = {
            'question': 'Тестовый вопрос для тестирования',
            'test': self.test.pk
        }
        url = reverse('testing:question-list')
        create_response = self.client.post(url, db_create)
        print(f'лог: {create_response}, {create_response.json()}')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            Question.objects.filter(question='Тестовый вопрос для тестирования').count(), 1
        )

    def test_question_list_get(self):
        """Юниттест вывода списка вопросов"""
        url = reverse('testing:question-list')
        get_list_response = self.client.get(url)
        print(f'лог: {get_list_response}, {get_list_response.json()}')
        self.assertEqual(get_list_response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            get_list_response.json(),
            {'count': 1, 'next': None, 'previous': None,
             'results': [
                 {'id': self.question.pk, 'question': 'Эталонный вопрос для эталонного теста', 'test': self.test.pk}]}
        )

    def test_question_retrieve(self):
        """Юниттест вывода детализации вопроса"""
        url = reverse('testing:question-detail', args=(self.question.pk,))
        detail_response = self.client.get(url)
        print(f'лог: {detail_response.json()}')
        self.assertEqual(detail_response.status_code, status.HTTP_200_OK)
        self.assertEqual(detail_response.data['question'], 'Эталонный вопрос для эталонного теста')

    def test_question_delete(self):
        """Юниттест удаления вопроса"""
        url = reverse('testing:question-detail', args=(self.question.pk,))
        del_response = self.client.delete(url)
        print(f'лог: {del_response}')
        self.assertEqual(del_response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(
            Question.objects.filter(question='Эталонный вопрос для эталонного теста').count(), 0
        )

    def test_question_put(self):
        """Юниттест обновления вопроса через put"""
        db_put = {
            'question': 'Измененный вопрос',
            'test': self.test.pk
        }
        url = reverse('testing:question-detail', args=(self.question.pk,))
        put_response = self.client.put(url, db_put)
        print(f'лог: {put_response}')
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.data['question'], 'Измененный вопрос')

    def test_course_patch(self):
        """Юниттест обновления вопроса через patch"""
        db_patch = {
            'question': 'Еще раз измененный вопрос',
        }
        url = reverse('testing:question-detail', args=(self.question.pk,))
        patch_response = self.client.patch(url, db_patch)
        print(f'лог: {patch_response}')
        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(patch_response.data['question'], 'Еще раз измененный вопрос')


class AnswerAPITestCase(APITestCase):
    """Тесты для Вопроса"""

    def setUp(self):
        self.user = User.objects.create(email='course@user.com', password='123456', role='teacher')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            title='Эталонный курс', description='Эталонный курс для тестирования', owner=self.user)
        self.topic = Topic.objects.create(
            title='Эталонная тема', description='Эталонная тема для тестирования', course=self.course,
            owner=self.user)
        self.test = Test.objects.create(
            description='Эталонный тест для эталонной темы', topic=self.topic)
        self.question = Question.objects.create(
            question='Эталонный вопрос для эталонного теста', test=self.test)
        self.answer = Answer.objects.create(
            answer='Эталонный ответ для эталонного вопроса', is_correct=True, question=self.question)

    def test_answer_create(self):
        """Юниттест создания ответа"""
        db_create = {
            'answer': 'Тестовый ответ для тестирования',
            'question': self.question.pk
        }
        url = reverse('testing:answer-list')
        create_response = self.client.post(url, db_create)
        print(f'лог: {create_response}, {create_response.json()}')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            Answer.objects.filter(answer='Тестовый ответ для тестирования').count(), 1
        )

    def test_answer_list_get(self):
        """Юниттест вывода списка ответов"""
        url = reverse('testing:answer-list')
        get_list_response = self.client.get(url)
        print(f'лог: {get_list_response}, {get_list_response.json()}')
        self.assertEqual(get_list_response.status_code, status.HTTP_200_OK)

    def test_answer_retrieve(self):
        """Юниттест вывода детализации ответа"""
        url = reverse('testing:answer-detail', args=(self.answer.pk,))
        detail_response = self.client.get(url)
        print(f'лог: {detail_response.json()}')
        self.assertEqual(detail_response.status_code, status.HTTP_200_OK)
        self.assertEqual(detail_response.data['answer'], 'Эталонный ответ для эталонного вопроса')

    def test_answer_delete(self):
        """Юниттест удаления ответа"""
        url = reverse('testing:answer-detail', args=(self.answer.pk,))
        del_response = self.client.delete(url)
        print(f'лог: {del_response}')
        self.assertEqual(del_response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(
            Answer.objects.filter(answer='Эталонный ответ для эталонного вопроса').count(), 0
        )

    def test_answer_put(self):
        """Юниттест обновления ответа через put"""
        db_put = {
            'answer': 'Измененный ответ',
            'question': self.question.pk
        }
        url = reverse('testing:answer-detail', args=(self.answer.pk,))
        put_response = self.client.put(url, db_put)
        print(f'лог: {put_response}')
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.data['answer'], 'Измененный ответ')

    def test_course_patch(self):
        """Юниттест обновления ответа через patch"""
        db_patch = {
            'answer': 'Еще раз измененный ответ',
        }
        url = reverse('testing:answer-detail', args=(self.answer.pk,))
        patch_response = self.client.patch(url, db_patch)
        print(f'лог: {patch_response}')
        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(patch_response.data['answer'], 'Еще раз измененный ответ')