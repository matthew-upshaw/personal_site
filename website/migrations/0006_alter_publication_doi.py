# Generated by Django 4.1.7 on 2023-02-20 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_publication_doi_publication_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='doi',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]