from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

import json


class MainConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope["user"]
        self.group_name = f'individual_group_{self.user.id}'

        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        print('Joining group', self.group_name)
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def receive(self, text_data):
        json_data = json.loads(text_data)
        msg = json_data['message']
        if msg == 'equip':
            self.user.player.equip_item(json_data['id'])
        elif msg == 'sellItem':
            self.user.player.sell_item(json_data['id'])
        elif msg == 'buyItem':
            self.user.player.buy_item(json_data['name'])


    def set_energy_level(self, event):
        energy_level = event['energy_level']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'new_energy_level': energy_level
        }))
