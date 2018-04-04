# Generated by Django 2.0.4 on 2018-04-04 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Circle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='サークル名')),
                ('kind', models.CharField(choices=[('文化系', '文化系'), ('運動系', '運動系'), ('テニサー', 'テニサー')], max_length=4, verbose_name='種別')),
            ],
            options={
                'verbose_name': 'サークル',
                'verbose_name_plural': 'サークル',
            },
        ),
        migrations.CreateModel(
            name='Tadameshi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='開催日')),
                ('time', models.TimeField(verbose_name='集合時刻')),
                ('place', models.CharField(max_length=30, verbose_name='集合場所')),
                ('male', models.CharField(choices=[('OK', 'OK'), ('NG', 'NG'), ('不明', '不明')], default='OK', max_length=2, verbose_name='男性')),
                ('female', models.CharField(choices=[('OK', 'OK'), ('NG', 'NG'), ('不明', '不明')], default='OK', max_length=2, verbose_name='女性')),
                ('tobiiri', models.CharField(choices=[('OK', 'OK'), ('NG', 'NG'), ('不明', '不明')], default='不明', max_length=2, verbose_name='飛び入り参加可能')),
                ('note', models.TextField(blank=True, max_length=100, null=True, verbose_name='イベント名/会食場所/備考')),
                ('recommend', models.BooleanField(default=False, verbose_name='おすすめ')),
                ('circle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hontai.Circle', verbose_name='サークル')),
            ],
            options={
                'verbose_name': 'タダ飯',
                'verbose_name_plural': 'タダ飯',
            },
        ),
    ]
