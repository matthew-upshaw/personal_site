# Generated by Django 4.1.7 on 2023-02-20 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_alter_education_award_alter_education_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='is_dissertation',
            field=models.BooleanField(default=False),
        ),
    ]