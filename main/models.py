from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime

#from .models import PlayerItem
from main.model.Items import ALL_ITEMS


class Question(models.Model):
    def __str__(self):
        return self.question_text
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Player(models.Model):
    max_energy = 100
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    energy = models.IntegerField(default=max_energy)
    max_energy = models.IntegerField(default=max_energy)

    gold = models.IntegerField(default=0)

    strength = models.IntegerField(default=22)
    dexterity = models.IntegerField(default=18)
    intelligence = models.IntegerField(default=20)
    hp = models.IntegerField(default=100)
    max_hp = models.IntegerField(default=100)

    current_town = models.CharField(default='Espin', max_length=100)

    def equiped_item_map(self):
        # TODO: optimization This should only be called once per page request, and cached in a variable
        return {eq_item.item().eq_slot.name: eq_item for eq_item in self.eq_items.all()}

    def get_equiped_item(self, slot):
        eq_item_map = self.equiped_item_map()
        return eq_item_map[slot] if slot in eq_item_map else None

    def equip_item(self, player_item_id):
        # terribly inefficient
        player_item = next(x for x in self.items.all() if str(x.id) == player_item_id)
        if player_item.player_eq is None:
            slot = player_item.item().eq_slot
            # Unequip current
            for current_item in self.eq_items.all():
                if current_item.item().eq_slot == slot:
                    current_item.player_eq = None
                    current_item.save()
                    break
            # Equip this one
            player_item.player_eq = self
            player_item.save()
        else:
            player_item.player_eq = None
            player_item.save()

    def sell_item(self, player_item_id):
        # terribly inefficient
        items = self.items.all()
        player_item = next(x for x in items if str(x.id) == player_item_id)
        self.gold += player_item.item().price
        self.save()
        player_item.delete()

    def buy_item(self, item_name):
        item = ALL_ITEMS[item_name]
        if self.gold - item.shop_price >= 0:
            self.gold -= item.shop_price
            self.save()
            pi = PlayerItem()
            pi.name = item_name
            pi.player = self
            pi.save()



class PlayerItem(models.Model):
    name = models.CharField(max_length=100)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='items')
    player_eq = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='eq_items', blank=True, null=True)

    def item(self):
        return ALL_ITEMS[self.name]
