# Generated by Django 4.0.5 on 2022-06-17 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_data', '0001_initial'),
    ]

    operations = [
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
                'verbose_name_plural': 'TestsData',
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='question',
            name='test_data',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='test_data.testdata', verbose_name='Тест'),
            preserve_default=False,
        ),
    ]
