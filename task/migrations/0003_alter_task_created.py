# Generated by Django 5.0.1 on 2024-01-07 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_remove_task_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
