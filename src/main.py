from src.models import Board, Continent, Region, Player, Unit


def print_board(board):
    for region in board.regionList:
        if region.owner is None:
            print("region {}: O".format(region.name))
        else:
            print("region {}: {}".format(region.name, region.owner))


def initialize_board():
    region_1 = Region("one", 1, 1, 1, 1)
    region_2 = Region("two", 2, 2, 1, 1)
    region_3 = Region("three", 3, 3, 1, 1)
    region_4 = Region("four", 4, 4, 1, 1)
    Region.add_neighbours(region_1, region_2)
    Region.add_neighbours(region_2, region_3)
    Region.add_neighbours(region_3, region_4)
    Region.add_neighbours(region_4, region_1)
    region_list = [region_1, region_2, region_3, region_4]
    continent_1 = Continent(2, [region_1, region_2])
    continent_2 = Continent(2, [region_3, region_4])
    continent_list = [continent_1, continent_2]
    board = Board(continent_list, region_list)
    return board


def initialize_players(nr_players):
    players = []
    for i in range(1, nr_players+1):
        player = Player("player_{}".format(i))
        players.append(player)
    return players


def initialize_unit_types():
    unit_type_list = []
    base_unit = Unit("base")
    unit_type_list.append(base_unit)
    return unit_type_list


def region_names(region_list):
    return [region.name for region in region_list]


def choose_land(board, player):
    region_name = input("{} choose a land to occupy, please refer to its name".format(player.name))
    succeeded = False
    for region in board.regionList:
        if region.name == region_name:
            region.change_owner(player.name)
            succeeded = True
    while not succeeded:
        print("please put in a valid name, one of the following:")
        print(region_names(board.regionList))
        region_name = input("player {} choose a land to occupy".format(player.name))
        for region in board.regionList:
            if region.name == region_name:
                region.change_owner(player.name)
                succeeded = True


def all_lands_owned(board):
    for region in board.regionList:
        if region.owner is None:
            return False
    else:
        return True


def players_choose_lands(board, players):
    print_board(board)
    while not all_lands_owned(board):
        for player in players:
            choose_land(board, player)
        print("Current State:")
        print_board(board)


def add_unit(board, player, unit_types):
    region_name = input("{} choose a region to add a unit too".format(player.name))
    succeeded = False
    for region in board.regionList:
        if region.name == region_name:
            region.add_units(unit_types[0].copy_unit())
            succeeded = True
    while not succeeded:
        print("please put in a valid name, one of the following:")
        print(region_names(board.regionList))
        for region in board.regionList:
            if region.name == region_name:
                region.add_units(unit_types[0].copy_unit())
                succeeded = True


def play_turn(board, player, unit_types):
    print_board(board)
    add_unit(board, player, unit_types)


def game_loop(turn, board, players, unit_types):
    if turn == 0:
        players_choose_lands(board, players)
    for player in players:
        play_turn(board, player, unit_types)
    return True


def main():
    won = False
    board = initialize_board()
    players = initialize_players(2)
    unit_types = initialize_unit_types()
    turn = 0
    while not won:
        # make sure this is not an endless loop
        won = game_loop(turn, board, players, unit_types)


if __name__ == "__main__":
    main()
