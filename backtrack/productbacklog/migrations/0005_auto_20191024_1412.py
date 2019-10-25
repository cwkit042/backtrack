# Generated by Django 2.2.6 on 2019-10-24 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productbacklog', '0004_auto_20191022_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productbacklogitem',
            name='progress',
            field=models.CharField(choices=[('N', 'not start'), ('P', 'in progress'), ('C', 'complete')], default='N', max_length=1),
        ),
    ]
