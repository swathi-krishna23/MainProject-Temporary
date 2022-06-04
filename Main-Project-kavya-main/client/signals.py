from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Crashed_frames, Camera_info
from channels.layers import  get_channel_layer
from asgiref.sync import async_to_sync
import json


@receiver(post_save, sender=Crashed_frames)
def accident(sender, instance, created, **kwargs):
    if created:
        print("New entry in crashed frames table")
        print('save called')
        channel_layer = get_channel_layer()
        print(channel_layer)
        print(list(instance.__str__().split()))
        # print(type(instance.__str__()))
        value = getattr(instance, 'frame_id')
        print(value)
        print(instance.camera_id.location)
        
        data = { 'camera_id': instance.camera_id.camera_id, 'city': instance.camera_id.city, 'location':  instance.camera_id.location, 'frame_id': instance.frame_id}
        print(data)
        async_to_sync(channel_layer.group_send)(
            'test' , {
                'type' : 'send_notification',
                'event': 'New Notification',
                'value' : json.dumps(data)
            }
            
        )
        print(channel_layer)

