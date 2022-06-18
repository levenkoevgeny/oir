from django.db import migrations
from test_data.models import EmployeeKind, Subdivision, Faculty, Course, TestData, Question, Answer


def create_employee_kinds():
    employee_kinds = [
        {'id': 1, 'employee_kind': 'Курсант'},
        {'id': 2, 'employee_kind': 'Переменный состав'}
    ]

    EmployeeKind.objects.all().delete()

    for employee_kind in employee_kinds:
        EmployeeKind.objects.create(**employee_kind)


def create_faculties():
    faculties = [
        {'id': 1, 'faculty_name': 'ФКМ'},
        {'id': 2, 'faculty_name': 'ФМОБ'},
        {'id': 3, 'faculty_name': 'УИФ'},
        {'id': 4, 'faculty_name': 'СЭФ'}
    ]

    Faculty.objects.all().delete()

    for faculty in faculties:
        Faculty.objects.create(**faculty)


def create_courses():
    courses = [
        {'id': 1, 'course_name': '1'},
        {'id': 2, 'course_name': '2'},
        {'id': 3, 'course_name': '3'},
        {'id': 4, 'course_name': '4'}
    ]

    Course.objects.all().delete()

    for course in courses:
        Course.objects.create(**course)


def create_tests():
    TestData.objects.all().delete()
    test_data = [
        {'test_name': 'Тест № 1', 'extra_data': 'Первый тест', 'questions':
            [
                {'question_text': 'КАК ВЫ ОЦЕНИВАЕТЕ СВОЁ НАСТРОЕНИЕ В ПОСЛЕДНИЕ ДНИ?', 'has_multiple_choice': False,
                 'answers':
                     [
                         {
                             'answer_text': 'прекрасное настроение'
                         },
                         {
                             'answer_text': 'нормальное (обычное)'
                         },
                         {
                             'answer_text': 'испытываю напряжение, раздражение'
                         },
                         {
                             'answer_text': 'испытываю страх, тревогу'
                         },
                     ]
                 }

            ]
         }
    ]

    for test in test_data:
        new_test = TestData.objects.create(test_name=test['test_name'], extra_data=test['extra_data'])

        questions = test['questions']

        for question in questions:
            new_question = Question.objects.create(question_text=question['question_text'],
                                                   has_multiple_choice=question['has_multiple_choice'],
                                                   test_data=new_test)
            answers = question['answers']
            for answer in answers:
                Answer.objects.create(answer_text=answer['answer_text'], question=new_question)


def init_db(apps, schema_editor):
    create_employee_kinds()
    create_faculties()
    create_courses()
    create_tests()


class Migration(migrations.Migration):
    dependencies = [
        ('test_data', '0005_auto_20220618_1213'),
    ]

    operations = [
        migrations.RunPython(init_db),
    ]
