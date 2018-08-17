# Generated by Django 2.0.4 on 2018-08-09 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trader', '0003_book_runnerbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accuracy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dec', models.FloatField(null=True)),
                ('perc', models.FloatField(null=True)),
                ('won', models.NullBooleanField()),
                ('error', models.FloatField(null=True)),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trader.Market')),
                ('runner_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trader.RunnerBook')),
            ],
        ),
        migrations.CreateModel(
            name='ALog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dts', models.DateTimeField()),
                ('counter', models.IntegerField(null=True)),
                ('duration', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bet_id', models.BigIntegerField()),
                ('est', models.FloatField()),
                ('trade', models.FloatField(null=True)),
                ('back', models.FloatField(null=True)),
                ('lay', models.FloatField(null=True)),
                ('margin', models.FloatField()),
                ('bracket', models.IntegerField()),
                ('payout', models.FloatField()),
                ('liability', models.FloatField()),
                ('order_type', models.CharField(max_length=50)),
                ('persistence_type', models.CharField(max_length=50)),
                ('placed_at', models.DateTimeField()),
                ('price', models.FloatField()),
                ('size', models.FloatField()),
                ('side', models.CharField(max_length=20)),
                ('size_matched', models.FloatField(null=True)),
                ('size_remaining', models.FloatField(null=True)),
                ('size_lapsed', models.FloatField(null=True)),
                ('size_cancelled', models.FloatField(null=True)),
                ('size_voided', models.FloatField(null=True)),
                ('status', models.CharField(max_length=30)),
                ('outcome', models.CharField(max_length=50, null=True)),
                ('profit', models.FloatField(null=True)),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trader.Market')),
                ('runner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trader.Runner')),
            ],
        ),
        migrations.CreateModel(
            name='BFChamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mcid', models.IntegerField(null=True)),
                ('bfid', models.IntegerField()),
                ('lid', models.IntegerField(db_index=True, null=True)),
                ('sport', models.IntegerField(null=True)),
                ('country_code', models.CharField(max_length=2, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('gender', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BFEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meid', models.IntegerField(null=True)),
                ('bfid', models.IntegerField()),
                ('lid', models.IntegerField(db_index=True, null=True)),
                ('rid1', models.IntegerField(null=True)),
                ('rid2', models.IntegerField(null=True)),
                ('dt', models.DateTimeField(db_index=True, null=True)),
                ('dtc', models.DateTimeField(db_index=True, null=True)),
                ('dtip', models.DateTimeField(null=True)),
                ('status', models.IntegerField(null=True)),
                ('reversed', models.IntegerField(null=True)),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='trader.BFChamp')),
            ],
        ),
        migrations.CreateModel(
            name='BFOdds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b1odds', models.FloatField()),
                ('b2odds', models.FloatField()),
                ('b1size', models.FloatField(null=True)),
                ('b2size', models.FloatField(null=True)),
                ('l1odds', models.FloatField()),
                ('l2odds', models.FloatField()),
                ('l1size', models.FloatField(null=True)),
                ('l2size', models.FloatField(null=True)),
                ('dtc', models.DateTimeField(db_index=True, null=True)),
                ('ip', models.NullBooleanField()),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='trader.BFEvent')),
            ],
        ),
        migrations.CreateModel(
            name='BFPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mpid', models.IntegerField(null=True)),
                ('lid', models.IntegerField(db_index=True, null=True)),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('gender', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bucket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bins', models.IntegerField()),
                ('left', models.FloatField()),
                ('right', models.FloatField()),
                ('total', models.IntegerField()),
                ('count', models.IntegerField()),
                ('win_mean', models.FloatField()),
                ('coef', models.FloatField()),
                ('intercept', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='bfevent',
            name='pid1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='player1', to='trader.BFPlayer'),
        ),
        migrations.AddField(
            model_name='bfevent',
            name='pid2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='player2', to='trader.BFPlayer'),
        ),
    ]