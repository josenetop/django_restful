# Generated by Django 2.2 on 2019-04-18 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]