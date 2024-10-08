from rest_framework import serializers
from materials.models import Course, Topic, Lecture
from materials.validators import VideoValidator


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с контроллером создания Учебного курса"""
    topics = serializers.SerializerMethodField()

    def get_topics(self, course):
        topics_count = Topic.objects.filter(course=course).count()
        topics_list = [topic.title for topic in Topic.objects.filter(course=course)]
        return {"topics_count": topics_count, "topics_list": topics_list}

    class Meta:
        model = Course
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с контроллером создания Темы курса"""
    lectures = serializers.SerializerMethodField()

    def get_lectures(self, topic):
        lectures_count = Lecture.objects.filter(topic=topic).count()
        lectures_list = [lecture.title for lecture in Lecture.objects.filter(topic=topic)]
        return {"lectures_count": lectures_count, "lectures_list": lectures_list}

    class Meta:
        model = Topic
        fields = '__all__'


class LectureSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с контроллером создания Лекции"""

    class Meta:
        model = Lecture
        fields = '__all__'
        validators = [VideoValidator(field='video')]
