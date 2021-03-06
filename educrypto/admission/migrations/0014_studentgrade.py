# Generated by Django 4.0.2 on 2022-04-15 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0013_facultysubjectmap_rename_branch_faculty_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_uid', models.CharField(blank=True, max_length=200)),
                ('testName', models.CharField(blank=True, max_length=200)),
                ('branch', models.CharField(blank=True, max_length=200)),
                ('subject', models.CharField(blank=True, max_length=200)),
                ('marks', models.IntegerField()),
            ],
        ),
    ]
