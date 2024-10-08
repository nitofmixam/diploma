from django.contrib import admin
from materials.models import Course, Topic, Lecture


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Админка для модели Учебный курс"""
    list_display = ('id', 'title', 'description', 'owner',)
    search_fields = ('title', 'description',)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    """Админка для модели Тема курса"""
    list_display = ('id', 'course', 'title', 'description', 'owner',)
    list_filter = ('course',)
    search_fields = ('title', 'description',)


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    """Админка для модели Лекция"""
    list_display = ('id', 'topic', 'title', 'description', 'content', 'video', 'owner',)
    list_filter = ('topic',)
    search_fields = ('title', 'description',)