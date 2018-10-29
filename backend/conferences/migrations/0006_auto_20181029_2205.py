# Generated by Django 2.1.1 on 2018-10-29 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0005_auto_20181029_2156'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='track',
            options={'verbose_name': 'Track', 'verbose_name_plural': 'Tracks'},
        ),
        migrations.AlterField(
            model_name='conference',
            name='tracks',
            field=models.ManyToManyField(to='conferences.Track', verbose_name='tracks'),
        ),
    ]
