import os 
import django
import random
from django.apps import registry

from result import returnResult

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from client.models import Camera_info, Crashed_frames
ans=returnResult()
print(ans)
if(ans):
    camera_id_ = random.randint(1,10)
    frame_id = random.randint(1,200)

    camera = Camera_info.objects.get(camera_id=camera_id_)
    new_obj = Crashed_frames.objects.create(camera_id=camera, frame_id=frame_id)
    print(new_obj)


# user = User.objects.only('id').get(id=data['user_id'])
# obj = ModelA.objects.create(phone=data['phone'], user=user)
