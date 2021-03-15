import random


class Adventurer:
    """
    The adventurer has a finite carry capacity.  They cannot carry more than their carry_weight.  They also contain
    a coin_purse to keep all of their different coins that sum up to a total value.
    """

    def __init__(self, carry_weight):
        self.carry_weight = carry_weight
        self.coin_purse = {}
        self.inventory = []

    def show_inventory(self):
        """
        Shows Inventory
        :return: A String representation of the players inventory.
        """

        """
        === SAMPLE SHOW INVENTORY ===
        Adventurer (Total Carry Capacity: 100)
        Total Carry Weight: 70
        Total Carry Value: 537
        Total Coin Purse Value: 89

        == COINS ==
        bronze (1): 0
        copper (2): 0
        nickel (5): 1
        silver (13): 0
        gold (20): 1
        diamond (32): 2
        lunastone (100): 0

        == INVENTORY ==
        dagger: Wgt=4, V=90
        armor: Wgt=52, V=118
        herbs: Wgt=1, V=19
        herbs: Wgt=2, V=17
        clothing: Wgt=5, V=43
        dagger: Wgt=4, V=60
        jewels: Wgt=2, V=190
        """
        pass


class Chest:
    """
    A chest is a container of Items that can be randomly populated.
    """

    def __init__(self, n=10):
        self.contents = []
        for i in range(n):
            self.contents.append(Item.generate_random_item())

    def __str__(self):
        ret_str = ""
        x = 1
        tot_wgt = 0
        tot_val = 0
        for i in self.contents:
            ret_str += f'{x}: {i} \n'
            tot_wgt += i.weight
            tot_val += i.value
            x += 1
        return f"Chest: Item Count={X}, Total Value={tot_val}, Total Weight={tot_wgt}\n{ret_str}"

    def remove(self, item):
        """
        Removes the provided item from the chest.
        :param item: The item object that should be remove from the list.
        :return: True if item was found/removed, False otherwise
        """
        try:
            self.contents.remove(item)
            return True
        except ValueError as e:
            return False

class Item:
    """
    An Item can be of multiple types and those types have a min and max value and weight.  When an item of a specific
    type is generated, it should contain a value that is within that range.  To add different types to the game,
    simply add them to the static field Item.TYPES as shown.  This is used by the generator to create a random item.
    """
    TYPES = {
        'dagger':
            {
                'weight': (1, 5),
                'value': (10, 100)
            },
        'jewels':
            {
                'weight': (1, 5),
                'value': (50, 500)
            },
        'clothing':
            {
                'weight': (5, 10),
                'value': (1, 50)
            },
        'herbs':
            {
                'weight': (1, 2),
                'value': (3, 20)
            },
        'gems':
            {
                'weight': (1, 5),
                'value': (25, 250)
            },
        'armor':
            {
                'weight': (25, 75),
                'value': (50, 1000)
            }
    }

    def __init__(self, name, weight, value):
        """
        Creates an item with the provided type (name), weight and value.
        :param name: The name of the item.  Usually just the 'type' of item it is.
        :param weight: The weight of the item.  (numeric)
        :param value: The value of the item (int).
        """
        self.name = name
        self.weight = weight
        self.value = value

    def __str__(self):
        return f"{self.name}: Wgt={self.weight}, V={self.value}"

    @staticmethod
    def generate_random_item(of_type=None):
        """
        Will generate a random item of any type or of a specific type when provided.
        :param of_type: The TYPE of item to generate.  If omitted, the method will generate an item of random Type.
        :return: An instantiated Item.
        """
        if of_type is None:
            of_type = random.choice(list(Item.TYPES))

        w_min, w_max = Item.TYPES[of_type]['weight']
        v_min, v_max = Item.TYPES[of_type]['value']
        w = random.randint(w_min, w_max)
        v = random.randint(v_min, v_max)
        return Item(of_type, w, v)


class Game:
    """
    The controlller for the game controlling the different Coin Denominations and maintaining the states of chests and
    acting as the "shop" that can also sell the items for the Adventurer.
    """
    COINS = {
        1: 'bronze',
        2: 'copper',
        5: 'nickel',
        13: 'silver',
        20: 'gold',
        32: 'diamond',
        100: 'lunastone'
    }

    def __init__(self, player):
        self.player = player
        self.chests = []

    def show_player_inventory(self):
        print(player.show_inventory())

    def add_chest(self, chest):
        """
        Adds a chest to the game.
        :param chest: The Chest to add to the game.
        :return: None
        """
        self.chests.append(chest)

    def show_chests(self):
        """
        Prints a list of the chest contents to the screen.
        :return: None
        """

        """
        === SAMPLE SHOW CHESTS === 
        Chest 0:
        = CONTENTS =
        dagger: Wgt=4, V=90
        armor: Wgt=52, V=118
        herbs: Wgt=1, V=19
        herbs: Wgt=2, V=17
        clothing: Wgt=5, V=43
        dagger: Wgt=4, V=60
        jewels: Wgt=2, V=190

        Chest 1:
        = CONTENTS = 
        clothing: Wgt=5, V=43
        dagger: Wgt=4, V=60
        """
        pass

    def loot_chests(self):
        """
        For each chest in the game, determine the optimal content to remove [0-1] knapsack
        and add the item to the adventurers inventory.
        Chests may still have contents remaining after looting.

        Note after looting each chest, the remaining carry weight of the adventurer will be
        reduced.  The adventurer does NOT have to select the optional ORDER of looting chests
        if there are more than one.  For example if the first chest contains 100 lbs of clothes
        and the second contains 100 lbs of jewels, if the adventurer loots the clothing chest
        first, then the opportunity to loot the jewels will be missed.

        :return: None
        """
        pass

    def sell_items(self):
        """
        Sell items will take the entirety of the adventurers inventory, calculate its total
        value and "sell it." This will remove it all items from inventory and in return "payment"
        matching that total value will be added to the adventurer's coin_purse, consisting of the
        optimal set of denominations.  For example, if the total inventory is valued at 124, the
        coin_purse will have the following denominations added:
            1 Diamond (100 value)
            1 Gold (20 value)
            2 Nickel (2x2 = 4 value)

        :return: None
        """
        pass


if __name__ == "__main__":
    # CREATE A PLAYER WITH FINITE CARRY CAPACITY
    player = Adventurer(carry_weight=100)
    game = Game(player)

    # INDICATE THERE IS NO INVENTORY AND NO MONEY
    game.show_player_inventory()

    # CREATE CHESTS WITH RANDOM CONTENT AND ADD IT TO THE GAME
    game.add_chest(Chest())

    # SHOW THE CONTENT OF ANY CHESTS IN THE GAME
    game.show_chests()

    # THE GAME SHOULD HAVE A METHOD THAT WILL OPTIMALLY LOOT THE ITEMS
    # IN THE CHEST [0-1 KNAPSACK] AND ADD IT TO THE PLAYER'S INVENTORY
    # ANY ITEMS NO IN THE CHEST SHOULD REMAIN
    game.loot_chests()

    game.show_chests()
    game.show_player_inventory()

    # THE CAME SHOULD HAVE A METHOD TO TAKE INVENTORY FROM THE PLAYER
    # CONVERT IT INTO PROPER DENOMINATIONS, AND PLACE THAT DATA INTO THE COIN PURSE
    game.sell_items()

    game.show_player_inventory()





