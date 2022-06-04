from django.db import models

from channels.layers import  get_channel_layer
from asgiref.sync import async_to_sync
import json


class Camera_info(models.Model):

    camera_id = models.IntegerField()
    city = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return str(self.camera_id) + ' - ' + self.location


class Crashed_frames(models.Model):

    camera_id = models.ForeignKey(Camera_info, on_delete=models.CASCADE)
    frame_id = models.IntegerField()
    img = models.ImageField(upload_to='pics', default='-')
    video = models.FileField(null=True)
    crash_time = models.DateTimeField(auto_created=True)

    def __str__(self):
        return str(self.camera_id) + ' - ' + str(self.crash_time)