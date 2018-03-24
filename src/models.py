class Player(object):
    """
        A player owns regions and units. Not all units have to be placed when it is owned by a player.
        A player owns a region by placing a unit on top of it. So, maybe, the region is owned by the unit and the player
        does not have a list of regions?
    """
    def __init__(self, name):
        self.name = name
        self.units = []
        self.regions = []


class Board(object):
    """
        A board consists of multiple Regions and Continents.
    """

    def __init__(self, continents, regions):
        self.continentList = continents
        self.regionList = regions

    def get_region_by_name(self, name):
        for region in self.regionList:
            if region.name == name:
                return region


class Continent(object):
    """
        A continent is a collection of neighbours, which if owned by one player, give that player some extra score.
    """
    def __init__(self, score, regions):
        self.score = score
        self.regionList = regions


class Region(object):
    """
        A region has a list of neighbouring regions and for now is represented as a rectangle. Therefore it has an x, y
        and a size variable
        A region also has an owner and a list of units. Upon creation these are None.
    """
    def __init__(self, name, x, y, length, width):
        self.neighbours = []
        self.name = name
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.owner = None
        self.units = []

    # The added neighbour can be a either one entry, or a list.
    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)

    @staticmethod
    def add_neighbours(neighbour_1, neighbour_2):
        neighbour_1.add_neighbour(neighbour_2)
        neighbour_2.add_neighbour(neighbour_1)

    def change_owner(self, owner):
        self.owner = owner

    def add_units(self, units):
        if type(units) is list:
            for unit in units:
                self.units.append(unit)
        else:
            self.units.append(units)

    def remove_units(self, units):
        self.units.remove(units)

    def print_units(self):
        counts = {}
        for unit in self.units:
            name = unit.name
            if name in counts:
                counts[name]+= 1
            else:
                counts[name] = 1
        print("Units in this Region: {}".format(counts))


class Unit(object):
    """
        A Unit has a power and movement. Default for both is 1
    """
    def __init__(self, name, attack=1, defense=1, movement=1):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.movement = movement
        self.moved = 0

    def reset_movement(self):
        self.moved = 0

    def has_movement_left(self):
        if self.moved >= self.movement:
            return False
        else:
            return True

    def count_movement_left(self):
        return self.movement - self.moved

    def __str__(self):
        return self.name


class Soldier(Unit):
    def __init__(self):
        super().__init__("Soldier", 1, 1, 1)


class Horse(Unit):
    def __init__(self):
        super().__init__("Horse", 2, 1, 3)


class Action(object):
    pass
