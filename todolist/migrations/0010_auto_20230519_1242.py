# Generated by Django 3.0.5 on 2023-05-19 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0009_auto_20230519_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todotask',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]