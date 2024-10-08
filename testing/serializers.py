from rest_framework import serializers
from testing.models import Question, Answer, Test


class QuestionSerializer(serializers.ModelSerializer):
    """ Cериализатор для контроллеров Questions """

    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    """ Cериализатор для контроллеров Answers """

    class Meta:
        model = Answer
        fields = ('answer',)


class TestSerializer(serializers.ModelSerializer):
    """ Сериализатор для контроллеров Tests """

    class Meta:
        model = Test
        fields = '__all__'
