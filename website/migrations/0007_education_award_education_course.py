# Generated by Django 4.1.7 on 2023-02-20 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_publication_doi'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='award',
            field=models.JSONField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='education',
            name='course',
            field=models.JSONField(default=''),
            preserve_default=False,
        ),
    ]
