# Generated by Django 4.0.4 on 2022-04-30 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnergyUsage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=20, verbose_name='빌딩 이름')),
                ('daq_time', models.DateTimeField(verbose_name='일시')),
                ('wday', models.IntegerField(blank=True, null=True, verbose_name='요일')),
                ('day_type', models.IntegerField(blank=True, null=True, verbose_name='구분')),
                ('hour', models.IntegerField(blank=True, null=True, verbose_name='시간')),
                ('temp', models.FloatField(blank=True, null=True, verbose_name='온도')),
                ('rh', models.FloatField(blank=True, null=True, verbose_name='습도')),
                ('p_usage', models.FloatField(blank=True, null=True, verbose_name='전기 사용량')),
            ],
            options={
                'verbose_name': '에너지 사용량',
                'verbose_name_plural': '에너지 사용량',
                'db_table': 'energy_usage',
                'ordering': ['-daq_time'],
                'managed': True,
                'unique_together': {('b_name', 'daq_time')},
            },
        ),
    ]
