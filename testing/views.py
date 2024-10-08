from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from paginators import AppPagination
from testing.models import Test, Question, Answer
from testing.serializers import TestSerializer, QuestionSerializer, AnswerSerializer


class TestViewSet(viewsets.ModelViewSet):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    pagination_class = AppPagination


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    pagination_class = AppPagination


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    pagination_class = AppPagination


class GetQuestions(APIView):
    """Список вопросов в тесте по id теста."""
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        test = Test.objects.get(pk=kwargs["topic_pk"])
        questions_list = test.question_set.all().values()
        return Response({"Вопросы": list(questions_list)})


class GetAnswers(APIView):
    """Список ответов в тесте по id вопроса."""
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        question = Question.objects.get(pk=kwargs["question_pk"])
        answers_list = question.answer_set.all().values()
        return Response({"Варианты ответов на вопрос": list(answers_list)})


class GetIsCorrectAnswer(APIView):
    """Получение правильного ответа по id вопроса."""
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        question = Question.objects.get(pk=kwargs["question_pk"])
        answer_list = question.answer_set.filter(is_correct=True).values()
        return Response({"Правильный ответ": list(answer_list)})


class AnswerCheck(APIView):
    """Проверка правильности ответа по id вопроса и id ответа."""
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        question_pk = kwargs["question_pk"]
        answer_pk = kwargs["answer_pk"]

        question = Question.objects.get(pk=question_pk)
        answers_list = question.answer_set.filter(is_correct=True).values()
        pk_list = []

        for item in answers_list:
            pk_list.append(item["id"])
        if answer_pk in pk_list:
            message = "Правильно"
        else:
            message = "Ошибка"

        return Response({"message": message})