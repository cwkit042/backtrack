# Generated by Django 2.2.6 on 2019-10-24 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprintbacklog', '0003_auto_20191010_0936'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sprint',
            old_name='project',
            new_name='product',
        ),
    ]