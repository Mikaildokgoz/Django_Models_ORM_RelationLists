# Generated by Django 4.0.4 on 2022-05-18 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fscohort', '0004_student_year_in_school'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctors_name', models.CharField(max_length=50)),
            ],
        ),
    ]
