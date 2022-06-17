from django.contrib import admin
from .models import EmployeeKind, Subdivision, Faculty, Course, QuestionaryData, TestData, Question, Answer, TestResult


admin.site.register(EmployeeKind)
admin.site.register(Subdivision)
admin.site.register(Faculty)
admin.site.register(Course)
admin.site.register(QuestionaryData)
admin.site.register(TestData)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(TestResult)
