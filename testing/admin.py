from django.contrib import admin
from testing.models import Test, Question, Answer
import nested_admin


# Мульти-админка с вложенными строками
class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
    extra = 0


class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [AnswerInline]
    extra = 0


class TestAdmin(nested_admin.NestedModelAdmin):
    model = Test
    inlines = [QuestionInline]
    extra = 0


admin.site.register(Test, TestAdmin)