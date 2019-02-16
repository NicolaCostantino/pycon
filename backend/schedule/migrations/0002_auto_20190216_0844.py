# Generated by Django 2.1.5 on 2019-02-16 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduleitem',
            name='room',
        ),
        migrations.AddField(
            model_name='scheduleitem',
            name='rooms',
            field=models.ManyToManyField(related_name='talks', to='schedule.Room', verbose_name='rooms'),
        ),
    ]