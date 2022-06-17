# Generated by Django 4.0.5 on 2022-06-17 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=255, verbose_name='Текст вопроса')),
                ('has_multiple_choice', models.BooleanField(verbose_name='Множественные ответы(checkbox)')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='TestDataFirst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_kind', models.IntegerField(choices=[('1', 'Курсант'), ('2', 'Переменный состав')], verbose_name='Вид сотрудника')),
            ],
            options={
                'verbose_name': 'TestDataFirst',
                'verbose_name_plural': 'TestDataFirst',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=255, verbose_name='Текст ответа')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_data.question', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
                'ordering': ('id',),
            },
        ),
    ]
