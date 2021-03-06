# Generated by Django 4.0.2 on 2022-02-12 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0009_auto_20220124_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShareKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atp', models.CharField(blank=True, max_length=200)),
                ('third_party', models.CharField(blank=True, max_length=200)),
                ('doc_type', models.CharField(blank=True, max_length=200)),
                ('student_uid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admission.student')),
            ],
        ),
    ]
