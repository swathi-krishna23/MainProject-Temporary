from django.contrib import admin
from .models import Camera_info, Crashed_frames
# Register your models here.

admin.site.register(Crashed_frames)
admin.site.register(Camera_info)
