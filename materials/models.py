from django.db import models
from config import settings

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    """Класс для описания модели Учебный курс"""
    objects = None
    title = models.CharField(max_length=150, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание курса', **NULLABLE)
    imagery = models.ImageField(upload_to='materials/', verbose_name='Изображение(превью)', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Учебный курс'
        verbose_name_plural = 'Учебные курсы'


class Topic(models.Model):
    """Класс для описания модели Тема курса"""
    objects = None
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Учебный курс')
    title = models.CharField(max_length=150, verbose_name='Название темы курса')
    description = models.TextField(verbose_name='Описание темы', **NULLABLE)
    imagery = models.ImageField(upload_to='materials/', verbose_name='Изображение(превью)', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Тема курса'
        verbose_name_plural = 'Темы курса'


class Lecture(models.Model):
    """Класс для описания модели Лекция"""
    objects = None
    # topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='Тема')
    title = models.CharField(max_length=150, verbose_name='Название лекции к теме')
    description = models.TextField(verbose_name='Описание лекции', **NULLABLE)
    imagery = models.ImageField(upload_to='materials/', verbose_name='Изображение(превью)', **NULLABLE)
    content = models.FileField(upload_to='materials/', verbose_name='Содержание лекции', **NULLABLE)
    video = models.URLField(max_length=150, verbose_name='Ссылка на видео', **NULLABLE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='Тема')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Лекция'
        verbose_name_plural = 'Лекции'