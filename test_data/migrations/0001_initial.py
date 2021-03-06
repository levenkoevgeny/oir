# Generated by Django 3.2.7 on 2022-06-20 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=255, verbose_name='Текст ответа')),
                ('has_extra_data', models.BooleanField(default=False, verbose_name='Имеет дополнительную информацию')),
                ('index_number', models.IntegerField(blank=True, null=True, verbose_name='Порядковый номер ответа')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': '3 Answers',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=255, verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='EmployeeKind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_kind', models.CharField(max_length=255, verbose_name='Вид сотрудника')),
            ],
            options={
                'verbose_name': 'EmployeeKind',
                'verbose_name_plural': 'EmployeeKinds',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=255, verbose_name='Название факультета')),
            ],
            options={
                'verbose_name': 'Faculty',
                'verbose_name_plural': 'Faculties',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.IntegerField(choices=[(1, 'Single (radio)'), (2, 'Multiple (checkbox)'), (3, 'Text field')], default=1, verbose_name='Тип вопроса')),
                ('question_text', models.CharField(max_length=255, verbose_name='Текст вопроса')),
                ('index_number', models.IntegerField(blank=True, null=True, verbose_name='Порядковый номер вопроса')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': '2 Questions',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='QuestionaryData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='test_data.course', verbose_name='Курс')),
                ('employee_kind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_data.employeekind', verbose_name='Тип сотрудника')),
                ('faculty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='test_data.faculty', verbose_name='Факультет')),
            ],
            options={
                'verbose_name': 'QuestionaryData',
                'verbose_name_plural': 'QuestionaryData',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Subdivision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subdivision_name', models.CharField(max_length=255, verbose_name='Название подразделения')),
            ],
            options={
                'verbose_name': 'Subdivision',
                'verbose_name_plural': 'Subdivisions',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='TestData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=255, verbose_name='Название теста')),
                ('extra_data', models.TextField(blank=True, null=True, verbose_name='Дополнительная информация')),
                ('data_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'TestData',
                'verbose_name_plural': '1 TestsData',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField(blank=True, null=True, verbose_name='Ответ (текстовый)')),
                ('extra_data', models.TextField(blank=True, null=True, verbose_name='Дополнительная информация к ответу')),
                ('answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='test_data.answer', verbose_name='Ответ')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_data.question', verbose_name='Вопрос')),
                ('questionary_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_data.questionarydata', verbose_name='Данные анкеты')),
            ],
            options={
                'verbose_name': 'TestResult',
                'verbose_name_plural': '4 TestResults',
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='questionarydata',
            name='subdivision',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='test_data.subdivision', verbose_name='Подразделение'),
        ),
        migrations.AddField(
            model_name='question',
            name='test_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_data.testdata', verbose_name='Тест'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_data.question', verbose_name='Вопрос'),
        ),
    ]
