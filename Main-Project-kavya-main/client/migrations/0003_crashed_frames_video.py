# Generated by Django 4.0.5 on 2022-06-02 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_crashed_frames_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='crashed_frames',
            name='video',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
