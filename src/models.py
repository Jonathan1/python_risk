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
        A board consists of multiple Continents.
    """

    def __init__(self, continents):
        self.continentList = continents


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
    """
    def __init__(self, x, y, length, width):
        self.neighbours = []
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.owner = None


class Unit(object):

    def __init__(self, power, movement):
        self.power = power
        self.movement = movement
        self.owner = None
        self.location = None


class Action(object):
    pass
