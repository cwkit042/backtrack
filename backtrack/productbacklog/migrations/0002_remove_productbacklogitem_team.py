# Generated by Django 2.2.6 on 2019-10-10 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productbacklog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productbacklogitem',
            name='team',
        ),
    ]
