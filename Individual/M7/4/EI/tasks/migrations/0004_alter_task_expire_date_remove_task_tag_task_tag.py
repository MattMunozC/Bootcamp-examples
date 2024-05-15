# Generated by Django 5.0.4 on 2024-05-08 22:50

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_content_task_expire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='expire_date',
            field=models.DateField(default=datetime.date(2024, 5, 8)),
        ),
        migrations.RemoveField(
            model_name='task',
            name='tag',
        ),
        migrations.AddField(
            model_name='task',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.tag'),
        ),
    ]
