# Generated by Django 2.1.5 on 2019-02-06 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20190205_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_seeker',
            name='age',
            field=models.SmallIntegerField(default=30),
        ),
        migrations.AddField(
            model_name='job_seeker',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='job_seeker',
            name='phone',
            field=models.BigIntegerField(default=1111111111),
        ),
        migrations.AddField(
            model_name='job_seeker',
            name='resume',
            field=models.FileField(default='NULL', upload_to='uploads/'),
        ),
    ]
