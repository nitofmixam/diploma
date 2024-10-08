from django.urls import path
from rest_framework.routers import DefaultRouter
from testing.apps import TestingConfig
from testing.views import TestViewSet, QuestionViewSet, AnswerViewSet, GetQuestions, GetAnswers, GetIsCorrectAnswer, \
    AnswerCheck

app_name = TestingConfig.name

router = DefaultRouter()
router.register(r'test', TestViewSet, 'test')
router.register(r'question', QuestionViewSet, 'question')
router.register(r'answer', AnswerViewSet, 'answer')

urlpatterns = [
                  path("get/questions/<int:topic_pk>/", GetQuestions.as_view(), name="get_questions"),
                  path("get/answers/<int:question_pk>/", GetAnswers.as_view(), name="get_answers"),
                  path("get/is_correct_answer/<int:question_pk>/", GetIsCorrectAnswer.as_view(),
                       name="get_is_correct_answers"),
                  path("answer/verification/<int:question_pk>/<int:answer_pk>/", AnswerCheck.as_view(),
                       name="answer_verification"),
              ] + router.urls
