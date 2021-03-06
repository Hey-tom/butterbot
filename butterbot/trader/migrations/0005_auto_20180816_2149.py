# Generated by Django 2.0.4 on 2018-08-16 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trader', '0004_auto_20180809_2342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accuracy',
            name='market',
        ),
        migrations.RemoveField(
            model_name='accuracy',
            name='runner_book',
        ),
        migrations.RemoveField(
            model_name='bet',
            name='market',
        ),
        migrations.RemoveField(
            model_name='bet',
            name='runner',
        ),
        migrations.RemoveField(
            model_name='book',
            name='market',
        ),
        migrations.DeleteModel(
            name='Bucket',
        ),
        migrations.RemoveField(
            model_name='market',
            name='event',
        ),
        migrations.RemoveField(
            model_name='runner',
            name='market',
        ),
        migrations.RemoveField(
            model_name='runnerbook',
            name='book',
        ),
        migrations.RemoveField(
            model_name='runnerbook',
            name='runner',
        ),
        migrations.DeleteModel(
            name='Accuracy',
        ),
        migrations.DeleteModel(
            name='Bet',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Market',
        ),
        migrations.DeleteModel(
            name='Runner',
        ),
        migrations.DeleteModel(
            name='RunnerBook',
        ),
    ]
