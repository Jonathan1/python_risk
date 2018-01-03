from src.models import Board, Continent, Region, Player, Unit, Soldier, Horse


def print_board(board):
    for region in board.regionList:
        if region.owner is None:
            print("region {}, owner O, soldiers 0, horses 0, power 0".format(region.name))
        else:
            power = 0
            soldiers = 0
            horses = 0
            for unit in region.units:
                if unit.name == "Horse":
                    horses += 1
                elif unit.name == "Soldier":
                    soldiers += 1
                power += unit.power
            print("region {}, owner {}, soldiers {}, horses {},  power {}".format(region.name, region.owner, soldiers, horses, power))


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


def region_names(region_list):
    return [region.name for region in region_list]


def owned_region_names(region_list, player):
    return [region.name for region in region_list if region.owner == player.name]


def choose_land(board, player):
    region_name = input("{} choose a land to occupy, please refer to its name".format(player.name))
    succeeded = False
    for region in board.regionList:
        if region.name == region_name:
            if region.owner is not None:
                print("region is already taken")
                break
            region.change_owner(player.name)
            region.add_units(Soldier())
            succeeded = True
            break
    while not succeeded:
        print("please put in a valid name, one of the following:")
        print(region_names(board.regionList))
        region_name = input("player {} choose a land to occupy".format(player.name))
        for region in board.regionList:
            if region.name == region_name:
                if region.owner is not None:
                    print("region is already taken")
                    break
                region.change_owner(player.name)
                region.add_units(Soldier())
                succeeded = True
                break


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


def add_unit(board, player):
    region_name = input("{} choose a region to add a unit too".format(player.name))
    succeeded = False
    for region in board.regionList:
        if region.name == region_name:
            if region.owner != player.name:
                print("This region is not owned by you")
                break
            region.add_units(Soldier())
            succeeded = True
            break
    while not succeeded:
        print("please put in a valid name, one of the following:")
        print(owned_region_names(board.regionList, player))
        region_name = input("{} choose a region to add a unit too".format(player.name))
        for region in board.regionList:
            if region.name == region_name:
                if region.owner != player.name:
                    print("This region is not owned by you")
                    break
                region.add_units(Soldier())
                succeeded = True
                break


def play_turn(board, player):
    print_board(board)
    add_unit(board, player)


def game_loop(turn, board, players):
    if turn == 0:
        players_choose_lands(board, players)
    print("--------------------")
    print("START OF THE GAME!!!")
    print("--------------------")
    for player in players:
        play_turn(board, player)
    return True


def main():
    won = False
    board = initialize_board()
    players = initialize_players(2)
    turn = 0
    while not won:
        # make sure this is not an endless loop
        won = game_loop(turn, board, players)
    print("-------------------")
    print("The End State Was:")
    print_board(board)
    print("-----------------------")


if __name__ == "__main__":
    main()
