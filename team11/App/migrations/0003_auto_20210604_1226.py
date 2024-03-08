# Generated by Django 2.2.20 on 2021-06-04 12:26

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20210507_0735'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacherId', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='grade',
            name='teacherComment',
            field=ckeditor.fields.RichTextField(),
        ),
    ]