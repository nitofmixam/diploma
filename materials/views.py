from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from materials.models import Course, Topic, Lecture
from materials.serializers import CourseSerializer, TopicSerializer, LectureSerializer
from paginators import AppPagination
from users.permissions import IsOwner, IsTeacher, IsStudent


class CourseViewSet(viewsets.ModelViewSet):
    """ViewSet-класс для работы с моделью Учебный курс"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = AppPagination

    def perform_create(self, serializer):
        """Переопределение метода create, авторизованный пользователь создающий курс, является владельцем курса"""
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def get_permissions(self):
        """Разрешения:
        создание курса - пользователю группы teacher,
        просмотр списка курсов и детализации по курсу - любому авторизованному пользователю,
            для неавторизованных пользователей только чтение
        обновление и удаление курса - только Владельцу"""
        if self.action in ('retrieve', 'list'):
            self.permission_classes = [IsAuthenticatedOrReadOnly, ]
        elif self.action in ('update', 'partial_update', 'destroy'):
            self.permission_classes = [IsAuthenticated | IsOwner, ]
        elif self.action == 'create':
            self.permission_classes = [IsAuthenticated | IsTeacher, ]
        return super().get_permissions()


class TopicViewSet(viewsets.ModelViewSet):
    """ViewSet-класс для работы с моделью Тема курса"""
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()
    pagination_class = AppPagination

    def perform_create(self, serializer):
        """Переопределение метода create, авторизованный пользователь создающий курс, является владельцем курса"""
        new_topic = serializer.save()
        new_topic.owner = self.request.user
        new_topic.save()

    def get_permissions(self):
        """Разрешения:
        создание темы - пользователю группы teacher,
        просмотр списка тем и детализации по теме - любому авторизованному пользователю,
            для неавторизованных пользователей только чтение
        обновление и удаление темы - только Владельцу"""
        if self.action in ('retrieve', 'list'):
            self.permission_classes = [IsAuthenticatedOrReadOnly, ]
        elif self.action in ('update', 'partial_update', 'destroy'):
            self.permission_classes = [IsAuthenticated | IsOwner, ]
        elif self.action == 'create':
            self.permission_classes = [IsAuthenticated | IsTeacher, ]
        return super().get_permissions()


class LectureCreateAPIView(generics.CreateAPIView):
    """Generic-класс для создания лекции
    Разрешение на создание - пользователю группы teacher,"""
    serializer_class = LectureSerializer
    permission_classes = [IsAuthenticated | IsTeacher, ]

    def perform_create(self, serializer):
        """Переопределение метода create, авторизованный пользователь создающий лекцию, является владельцем лекции"""
        new_lecture = serializer.save()
        new_lecture.owner = self.request.user
        new_lecture.save()


class LectureUpdateAPIView(generics.UpdateAPIView):
    """Generic-класс для изменения лекции
    Разрешение на изменение - только Владельцу"""
    serializer_class = LectureSerializer
    queryset = Lecture.objects.all()
    permission_classes = [IsAuthenticated | IsOwner, ]


class LectureDestroyAPIView(generics.DestroyAPIView):
    """Generic-класс для удаления лекции
    Разрешение на удаление - только Владельцу"""
    serializer_class = LectureSerializer
    queryset = Lecture.objects.all()
    permission_classes = [IsAuthenticated | IsOwner, ]


class LectureListAPIView(generics.ListAPIView):
    """Generic-класс для просмотра списка лекций
    Разрешение на просмотр списка лекций - любому авторизованному пользователю,
        для неавторизованных пользователей только чтение"""
    serializer_class = LectureSerializer
    queryset = Lecture.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    pagination_class = AppPagination


class LectureRetrieveAPIView(generics.RetrieveAPIView):
    """Generic-класс для просмотра детализации лекции
    Разрешение на просмотр детализации лекций - только Владельцу
        и авторизованным пользователям из групп teacher и student"""
    serializer_class = LectureSerializer
    queryset = Lecture.objects.all()
    permission_classes = [IsAuthenticated | IsTeacher | IsStudent | IsOwner, ]