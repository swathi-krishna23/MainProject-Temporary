# from django.urls import path
# from . import consumers

# websocket_urlpatterns = [
#     path('ws/socket-server/', consumers.ClientConsumer.as_asgi()),
#     # path('ws/client/notifier/', consumers.ClientConsumer.as_asgi()),
#     path('notifications/', consumers.ClientConsumer.as_asgi())
    

# ]

# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.urls import path
# from client.consumers import ClientConsumer

# application = ProtocolTypeRouter({
#     "websocket": URLRouter([
#         path("/notifications/", ClientConsumer),
#         path("ws/client/notifier/", ClientConsumer)
#     ])
# })

from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/notifications/', consumers.ClientConsumer.as_asgi()),
    re_path(r'ws/socket-server/', consumers.ClientConsumer.as_asgi())

]

