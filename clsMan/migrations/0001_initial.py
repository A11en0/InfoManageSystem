# Generated by Django 2.0.3 on 2022-04-10 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassTable',
            fields=[
                ('clsID', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='班级编号')),
                ('clsName', models.CharField(max_length=100, verbose_name='班级名称')),
                ('clsDesc', models.CharField(blank=True, max_length=100, verbose_name='班级描述')),
            ],
            options={
                'verbose_name': '班级信息',
                'verbose_name_plural': '班级信息',
                'ordering': ['clsID', 'clsName'],
            },
        ),
    ]
