# Generated by Django 2.0 on 2017-12-19 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionary',
            name='description',
            field=models.CharField(max_length=2047),
        ),
    ]
