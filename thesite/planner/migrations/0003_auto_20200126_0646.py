# Generated by Django 3.0.2 on 2020-01-26 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_auto_20200126_0625'),
    ]

    operations = [
        migrations.RenameField(
            model_name='progress',
            old_name='question',
            new_name='prog_tracker',
        ),
    ]
