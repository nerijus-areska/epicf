from django.contrib.auth.models import User

from datetime import datetime

from main.models import Player
import channels.layers
from asgiref.sync import async_to_sync


def update_energy():
    ADD_ENERGY = 10
    channel_layer = channels.layers.get_channel_layer()

    # TODO: optimization - We should have a 'live' users list in Redis and either only work with them, or set the energy levels for all,
    # but then only send the channel_layer messages to the ones in the list
    players = Player.objects.all()
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'updating energy for', len(players), 'players')
    for player in players:
        if player.energy < player.max_energy:
            print('Adding', ADD_ENERGY, 'to', player.energy, 'for player', player.user.username)
            player.energy += ADD_ENERGY
            if player.energy > player.max_energy:
                player.energy = player.max_energy
            player.save()
            async_to_sync(channel_layer.group_send)(f'individual_group_{player.user_id}', {'type': 'set_energy_level', 'energy_level': player.energy})
