# Generated by Django 5.0.2 on 2024-02-13 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paragraph_app', '0004_paragraph_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='paragraph',
            name='description',
            field=models.CharField(default='empty', max_length=1000),
        ),
    ]
