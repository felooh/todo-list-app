# Generated by Django 3.0.5 on 2023-05-19 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0007_auto_20230519_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='todotask',
            name='deadline',
            field=models.DateTimeField(null=True),
        ),
    ]
