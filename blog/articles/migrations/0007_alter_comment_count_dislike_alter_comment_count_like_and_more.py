# Generated by Django 4.2.2 on 2023-06-21 15:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_rename_name_article_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='count_dislike',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='count_like',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 21, 18, 25, 34, 842146), verbose_name='Comment date'),
        ),
    ]