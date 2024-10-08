from django.db import models
from materials.models import Topic

NULLABLE = {'blank': True, 'null': True}


class Test(models.Model):
    """ Модель тестов для тем"""
    objects = None
    topic = models.ForeignKey(Topic, verbose_name='Тема', on_delete=models.CASCADE, **NULLABLE)
    description = models.TextField(verbose_name='Описание теста', **NULLABLE)

    def __str__(self):
        return f'Тест по теме {self.topic}'

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
        ordering = ('topic',)


class Question(models.Model):
    """ Модель вопросов к тестам """
    objects = None
    test = models.ForeignKey(Test, verbose_name='Тест', on_delete=models.CASCADE, **NULLABLE)
    question = models.CharField(max_length=200, verbose_name='Вопрос', **NULLABLE)

    def __str__(self):
        return f'{self.question}'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ('test',)


class Answer(models.Model):
    """ Модель ответов к вопросам """
    objects = None
    question = models.ForeignKey(Question, verbose_name='Вопрос', on_delete=models.CASCADE, **NULLABLE)
    answer = models.CharField(max_length=100, verbose_name='Ответ', **NULLABLE)
    is_correct = models.BooleanField(default=False, verbose_name="Правильный ответ")

    def __str__(self):
        return f'{self.question}: {self.is_correct}'

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'