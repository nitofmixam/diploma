from django.contrib.auth.models import Group
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Generic-класс для создания пользователя
        Разрешение на создание - любому пользователю"""
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        """Переопределение метода create
            преобразование пароля в токен
            если при регистрации пользователя выбрана роль teacher, то включать пользователя группу teacher
            если при регистрации пользователя выбрана роль student, то включать пользователя группу student"""
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        if user.role == 'teacher':
            group = Group.objects.get(name='teacher')
            group.user_set.add(user)
        elif user.role == 'student':
            group = Group.objects.get(name='student')
            group.user_set.add(user)
        user.save()


class UserUpdateAPIView(generics.UpdateAPIView):
    """Generic-класс для изменения пользователя
        Разрешение на изменение - только авторизованному пользователю"""
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    """Generic-класс для удаления пользователя
        Разрешение на удаление - только авторизованному пользователю"""
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    """Generic-класс для просмотра списка пользователей
           Разрешение на просмотр списка пользователей - только админу"""
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Generic-класс для просмотра детализации по пользователю
               Разрешение на просмотр детализации по пользователю - только админу"""
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()