# Generated by Django 4.1.7 on 2023-02-16 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='open',
            field=models.BooleanField(default=True),
        ),
    ]
