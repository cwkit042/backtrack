# Generated by Django 2.2.6 on 2019-10-24 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='type',
            field=models.CharField(choices=[('developer', 'developer'), ('product owner', 'product owner')], default='developer', max_length=10),
        ),
    ]