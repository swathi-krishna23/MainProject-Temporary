import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
  
class ClientConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'
        # self.channel_name = 'test'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        # self.channel_layer.group_add('test', self.channel_name)
        print(f"Added {self.channel_name} channel to test")
        print(f"Added {self.room_group_name} channel to test")
        self.accept()
        self.send(text_data=json.dumps({'status' : 'Added {self.channel_name} channel to test'}))
        
        # self.accept()
        self.user = self.scope["user"]
        # print(vars(self.user))
        # print(vars(self))
        self.send(text_data=json.dumps({'status' : 'connected from django channels'}))

        # self.send(text_data=json.dumps({
        #     'type':'connection_established',
        #     'message': 'You are now connected!'
        # }))

    # def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']
    #     print(self.channel_name)
    #     print(self.room_group_name)
    #     async_to_sync(self.channel_layer.group_send) (
    #         self.room_group_name,
    #         {
    #             'type': 'chat_message',
    #             'message': message
    #         }
    #     )

        # print(message)

        # self.send(text_data=json.dumps({
        #     'type': 'chat',
        #     'message': message
        # }))

    # def chat_message(self, event):
    #     # self.send('msg received')
    #     # self.send('grp name', self.room_group_name)
    #     message = event['message']

    #     self.send(text_data=json.dumps({
    #             'type': 'chat',
    #             'message': message
    #     }))
         
         
    # def send_hello(self, event):
    #     print('hello')
    #     self.send('hello')
    # def send_notification(self, event):
    #     self.send_json(event)
        # self.send('send notification')
        # self.send_json(
        #     {
        #         'type': 'sned.notification',
        #         'content': event['value']
        #     }
        # )
        # # data = json.loads(event.get('value'))
        # # self.send(text_data=json.dumps({'payload' : data}))
        # # print(f"Got message {event} at {self.channel_name}")
        # print('send notification')
        
        
    def send_notification(self , event):
        # self.send('send notification')
        print('send notification')
        data = json.loads(event.get('value'))
        ev = event.get('event')
        self.send(text_data=json.dumps({'payload' : data, 'event': ev}))
        
        print('send notification')
        
    def disconnect(self, close_code):
        self.channel_layer.group_discard("test", self.channel_name)
        print(f"Removed {self.channel_name} channel to test")