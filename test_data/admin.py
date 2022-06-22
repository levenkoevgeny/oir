from django.contrib import admin
from .models import EmployeeKind, Subdivision, Faculty, Course, QuestionaryData, TestData, Question, Answer, TestResult


admin.site.register(EmployeeKind)
admin.site.register(Subdivision)
admin.site.register(Faculty)
admin.site.register(Course)
admin.site.register(TestData)


@admin.register(Question)
class QuestionPageAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'question_type', 'test_data', 'index_number')
    list_display_links = ('question_text',)
    search_fields = ['question_text']
    list_filter = ('test_data',)
    list_editable = ['question_text', 'index_number']


@admin.register(Answer)
class AnswerPageAdmin(admin.ModelAdmin):
    list_display = ('answer_text', 'question', 'has_extra_data',)
    search_fields = ['answer_text']
    list_filter = ('question', 'question__test_data')


@admin.register(TestResult)
class TestResultPageAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'answer_text', 'extra_data')


@admin.register(QuestionaryData)
class QuestionaryDataPageAdmin(admin.ModelAdmin):
    list_display = ('employee_kind', 'subdivision', 'faculty', 'course')
    list_filter = ('test', 'employee_kind', 'subdivision', 'faculty', 'course')
