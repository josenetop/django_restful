# Generated by Django 2.2 on 2019-04-18 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment_review', '0001_initial'),
        ('core', '0003_pontoturistico_attractions'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='comments',
            field=models.ManyToManyField(to='comment_review.Comments'),
        ),
    ]
