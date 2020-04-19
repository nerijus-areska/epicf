from enum import Enum, auto


def forDjango(cls):
    cls.do_not_call_in_templates = True
    return cls


@forDjango
class EQ_SLOT(Enum):
    HEAD = auto()
    BODY = auto()
    LEGS = auto()
    FEET = auto()
    WEAPON = auto()


ARMOR_SLOTS = [EQ_SLOT.HEAD.name, EQ_SLOT.BODY.name, EQ_SLOT.LEGS.name, EQ_SLOT.FEET.name]


class Item:

    def __init__(self, name, price, item_type):
        self.name = name
        self.price = price
        self.item_type = item_type
        self.shop_price = round(price * 1.3)


class Armor(Item):

    def __init__(self, name, price, eq_slot, armor):
        super().__init__(name, price, 'armor')
        self.eq_slot = eq_slot
        self.armor = armor


class Weapon(Item):

    def __init__(self, name, price, eq_slot, damage):
        super().__init__(name, price, 'weapon')
        self.eq_slot = eq_slot
        self.damage = damage


ALL_ITEMS = {
    'Iron helmet': Armor('Iron helmet', price=4, eq_slot=EQ_SLOT.HEAD, armor=33),
    'Wooden helmet': Armor('Wooden helmet', price=1, eq_slot=EQ_SLOT.HEAD, armor=1),
    'Iron boots': Armor('Iron boots', price=3, eq_slot=EQ_SLOT.FEET, armor=2),
    'Iron leggings': Armor('Iron leggings', price=3, eq_slot=EQ_SLOT.LEGS, armor=2),
    'Iron breastplate': Armor('Iron breastplate', price=10, eq_slot=EQ_SLOT.BODY, armor=5),
    'Iron sword': Weapon('Iron sword', price=4, eq_slot=EQ_SLOT.WEAPON, damage=7),
    'Wooden sword': Weapon('Iron sword', price=2, eq_slot=EQ_SLOT.WEAPON, damage=3),
}
