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
        {'faculty_name': 'ФКМ'},
                 {'faculty_name': 'ФМОБ'},
                 {'faculty_name': 'УИФ'},
                 {'faculty_name': 'СЭФ'}
                 ]

    Faculty.objects.all().delete()

    for faculty in faculties:
        Faculty.objects.create(**faculty)


def init_db(apps, schema_editor):
    create_employee_kinds()


class Migration(migrations.Migration):
    dependencies = [
        ('test_data', '0004_employeekind_alter_questionarydata_employee_kind'),
    ]

    operations = [
        migrations.RunPython(init_db),
    ]
