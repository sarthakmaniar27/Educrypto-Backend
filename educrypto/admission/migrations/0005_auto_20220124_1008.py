# Generated by Django 3.1.7 on 2022-01-24 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0004_auto_20220124_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdocument',
            name='aadhar_card',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='studentdocument',
            name='cet_scorecard',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='studentdocument',
            name='leaving_certificate',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='studentdocument',
            name='tenth_marksheet',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='studentdocument',
            name='twelfth_marksheet',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
