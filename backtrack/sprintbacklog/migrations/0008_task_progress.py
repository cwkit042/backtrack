# Generated by Django 2.2.6 on 2019-10-24 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprintbacklog', '0007_auto_20191024_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='progress',
            field=models.CharField(choices=[('N', 'not start'), ('P', 'in progress'), ('C', 'complete')], default='N', max_length=1),
        ),
    ]
