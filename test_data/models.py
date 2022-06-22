from django.db import models


SINGLE = 1
MULTIPLE = 2
TEXT = 3

QUESTION_TYPE_CHOICES = (
    (SINGLE, 'Single (radio)'),
    (MULTIPLE, 'Multiple (checkbox)'),
    (TEXT, 'Text field'),
)


class EmployeeKind(models.Model):
    employee_kind = models.CharField(verbose_name="Вид сотрудника", max_length=255)

    def __str__(self):
        return self.employee_kind

    class Meta:
        ordering = ('id',)
        verbose_name = 'EmployeeKind'
        verbose_name_plural = 'EmployeeKinds'


class Subdivision(models.Model):
    subdivision_name = models.CharField(verbose_name="Название подразделения", max_length=255)

    def __str__(self):
        return self.subdivision_name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Subdivision'
        verbose_name_plural = 'Subdivisions'


class Faculty(models.Model):
    faculty_name = models.CharField(verbose_name="Название факультета", max_length=255)

    def __str__(self):
        return self.faculty_name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'


class Course(models.Model):
    course_name = models.CharField(verbose_name="Курс", max_length=255)

    def __str__(self):
        return self.course_name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class QuestionaryData(models.Model):
    employee_kind = models.ForeignKey(EmployeeKind, verbose_name="Тип сотрудника", on_delete=models.CASCADE)
    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE, verbose_name="Подразделение", blank=True,
                                    null=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, verbose_name="Факультет", blank=True,
                                null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс", blank=True,
                               null=True)

    def __str__(self):
        return self.employee_kind.employee_kind

    class Meta:
        ordering = ('id',)
        verbose_name = 'QuestionaryData'
        verbose_name_plural = 'QuestionaryData'


class TestData(models.Model):
    test_name = models.CharField(verbose_name="Название теста", max_length=255)
    extra_data = models.TextField(verbose_name="Дополнительная информация", blank=True, null=True)
    data_created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    def __str__(self):
        return self.test_name

    class Meta:
        ordering = ('id',)
        verbose_name = 'TestData'
        verbose_name_plural = '1 TestsData'


class Question(models.Model):
    question_type = models.IntegerField(verbose_name="Тип вопроса", choices=QUESTION_TYPE_CHOICES, default=SINGLE)
    test_data = models.ForeignKey(TestData, on_delete=models.CASCADE, verbose_name="Тест")
    question_text = models.CharField(verbose_name="Текст вопроса", max_length=255)
    index_number = models.IntegerField(verbose_name="Порядковый номер вопроса", blank=True, null=True)

    def __str__(self):
        return self.question_text + ' ' + str(self.question_type)

    class Meta:
        ordering = ('index_number',)
        verbose_name = 'Question'
        verbose_name_plural = '2 Questions'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Вопрос")
    answer_text = models.CharField(verbose_name="Текст ответа", max_length=255)
    has_extra_data = models.BooleanField(verbose_name="Имеет дополнительную информацию", default=False)
    index_number = models.IntegerField(verbose_name="Порядковый номер ответа", blank=True, null=True)

    def __str__(self):
        return self.answer_text

    class Meta:
        ordering = ('id',)
        verbose_name = 'Answer'
        verbose_name_plural = '3 Answers'


class TestResult(models.Model):
    questionary_data = models.ForeignKey(QuestionaryData, on_delete=models.CASCADE, verbose_name="Данные анкеты")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Вопрос")
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, verbose_name="Ответ", blank=True, null=True)
    answer_text = models.TextField(verbose_name="Ответ (текстовый)", blank=True, null=True)
    extra_data = models.TextField(verbose_name="Дополнительная информация к ответу", blank=True, null=True)

    def __str__(self):
        return self.questionary_data.employee_kind.employee_kind + ' ' + self.question.question_text

    class Meta:
        ordering = ('id',)
        verbose_name = 'TestResult'
        verbose_name_plural = '4 TestResults'
