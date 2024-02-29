# Generated by Django 5.0.2 on 2024-02-13 13:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paragraph_app', '0005_paragraph_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200, null=True)),
                ('paragraph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='paragraph_app.paragraph')),
            ],
        ),
    ]
