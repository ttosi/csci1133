from enum import Enum
from random import randrange, randint
from rich import print


# the direction the ship is facing
class Direction(Enum):
    HORT = 1
    VERT = 2


# the state of a grid square on the board
class State(Enum):
    EMPTY = "[blue3]·[/blue3]"
    MISS = "[bright_black]×[/bright_black]"
    SHIP_NO_HIT = "[bright_white]o[/bright_white]"
    SHIP_HIT = "[red]*[/red]"


# create a board to store the state of the game
def create_board():
    board = {}
    for row in "abcdefghij":
        board[row] = [State.EMPTY] * 10
    return board


# given a board, print it to the console
def print_board(board):
    print("[cyan]    1  2  3  4  5  6  7  8  9  10[/cyan]")
    print("   " + "-" * 30)
    for row in board:
        row_string = "[cyan]" + row + "[/cyan]" + " | "
        for col in range(10):
            row_string += board[row][col].value + "  "
        print(row_string)


# given two boards, print each board side-by-side to the console
def print_two_boards(board1, board2):
    col_string = "    1  2  3  4  5  6  7  8  9  10"
    col_divider = "   " + "-" * 30
    board1_rows = []
    board2_rows = []

    for row in board1:
        row_string = "[cyan]" + row + "[/cyan]" + " | "
        for col in range(10):
            row_string += board1[row][col].value + "  "
        board1_rows.append(row_string)

    for row in board2:
        row_string = "[cyan]" + row + "[/cyan]" + " | "
        for col in range(10):
            row_string += board2[row][col].value + "  "
        board2_rows.append(row_string)

    print(col_string + "\t" + col_string)
    print(col_divider + "\t" + col_divider)
    for i in range(10):
        print(board1_rows[i] + "\t" + board2_rows[i])


class Ship:
    def __init__(self, length: int, name: str):
        self.name = name
        self.length = length
        self.start = None
        self.dir = None
        self.coords = []
        self.num_hits = 0
        self.is_sunk = False
        self.coords = []

    def create(self, board, start_coord, dir):
        self.start = start_coord
        self.dir = dir
        is_valid_placement = True
        match self.dir:
            case Direction.HORT:
                if self.length + start_coord[1] - 1 > 10:
                    is_valid_placement = False
                else:
                    for col in range(self.length):
                        if board[self.start[0]][col + self.start[1] - 1] != State.EMPTY:
                            is_valid_placement = False
                            break
                        self.coords.append(self.start[0] + str(col + self.start[1] - 1))
                        board[self.start[0]][
                            col + self.start[1] - 1
                        ] = State.SHIP_NO_HIT
            case Direction.VERT:
                row_ord = ord(self.start[0])
                if row_ord + self.length - 1 > ord("j"):
                    is_valid_placement = False
                else:
                    for row in range(row_ord, row_ord + self.length):
                        if board[chr(row)][self.start[1] - 1] != State.EMPTY:
                            is_valid_placement = False
                            break
                        self.coords.append(chr(row) + str(self.start[1] - 1))
                        board[chr(row)][self.start[1] - 1] = State.SHIP_NO_HIT

        if not is_valid_placement:
            print("Ship cannot be placed there. Try again.")
            for coord in self.coords:
                board[coord[0]][int(coord[1:])] = State.EMPTY

        return is_valid_placement

    def check_for_hit(self, coord):
        is_hit = False
        coord = coord[0] + str(coord[1] - 1)

        if coord in self.coords:
            is_hit = True
            self.num_hits += 1
            if self.num_hits == self.length:
                if player == "player":
                    print("[bold green]You sunk my " + self.name + "!![/bold green]")
                else:
                    print("[bold red]I sunk your " + self.name + ".[/bold red]")

                self.is_sunk = True

        return is_hit


def is_grid_empty(board, coord):
    pass


def fire_shot(ships, board_ships, board_record, coord):
    result = False
    if (
        board_ships[coord[0]][coord[1] - 1] != State.EMPTY
        and board_ships[coord[0]][coord[1] - 1] != State.SHIP_NO_HIT
    ):
        return

    for ship in ships:
        result = ship.check_for_hit(coord)
        if result:
            break

    if result:
        board_ships[coord[0]][coord[1] - 1] = State.SHIP_HIT
        board_record[coord[0]][coord[1] - 1] = State.SHIP_HIT
    else:
        board_ships[coord[0]][coord[1] - 1] = State.MISS
        board_record[coord[0]][coord[1] - 1] = State.MISS

    # check if all ships are sunk for game win
    sunk_count = 0
    for ship in ships:
        if ship.is_sunk:
            sunk_count += 1

    if sunk_count == len(ships):
        return True


def computer_move():
    # initial pattern alternate rowODDS rowEVENS
    # if hit, try to follow the ship
    pass


def auto_setup_board(ships, board):
    for ship in ships:
        successful_placement = False
        while not successful_placement:
            row = "abcdefghij"[randrange(10)]
            col = randrange(10)
            dir = Direction.HORT if randint(0, 1) == 0 else Direction.VERT
            successful_placement = ship.create(board, [row, col], dir)


def get_valid_input(message):
    is_valid = False
    while not is_valid:
        coord = input(message)
        if int(coord[1:]) < 1 or int(coord[1:]) > 10 or coord[0] not in "abcdefghij":
            print("Invalid coordinate, please try again")
            continue

        is_valid = True

    return coord


if __name__ == "__main__":
    player = ""
    computer_ships = []
    player_ships = []
    player_board_ships = create_board()
    player_board_record = create_board()
    computer_board_ships = create_board()
    computer_board_record = create_board()

    computer_ships.append(Ship(5, "Carrier"))
    computer_ships.append(Ship(4, "Battleship"))
    computer_ships.append(Ship(3, "Cruiser"))
    computer_ships.append(Ship(3, "Sub"))
    computer_ships.append(Ship(2, "Destroyer"))

    player_ships.append(Ship(5, "Carrier"))
    player_ships.append(Ship(4, "Battleship"))
    player_ships.append(Ship(3, "Cruiser"))
    player_ships.append(Ship(3, "Sub"))
    player_ships.append(Ship(2, "Destroyer"))

    auto_setup_board(computer_ships, computer_board_ships)
    auto_setup_board(player_ships, player_board_ships)

    # player's board setup
    # for ship in player_ships:
    #     print_board(player_board_ships)

    #     coord = get_valid_input(f"Place your {ship.name} ( {'o ' * ship.length})? ")
    #     direction = input("Place is horizontally or vertically (H/v)? ")

    #     dir = Direction.HORT
    #     if direction == "v":
    #         dir = Direction.VERT

    #     ship.create(player_board_ships, [coord[0], int(coord[1:])], dir)

    print_two_boards(player_board_ships, player_board_record)

    #   input coord (e.g. "a1" or "d3", etc.)
    #   check for hit or miss on computer's ship board
    #   record hit or miss on the player's record board
    while True:
        player = "player"
        coord = get_valid_input("Coordinate of next shot? ")
        comp_is_game_over = fire_shot(
            computer_ships,
            computer_board_ships,
            player_board_record,
            [coord[0], int(coord[1:])],
        )

        # computers turn
        player = "comp"
        for i in range(15):
            row = "abcdefghij"[randrange(10)]
            col = randrange(10)
            player_is_game_over = fire_shot(
                player_ships,
                player_board_ships,
                computer_board_record,
                [row, col],
            )

        print_two_boards(player_board_ships, player_board_record)
        if comp_is_game_over:
            print("GAME OVER, YOU WON!")
            break

        if player_is_game_over:
            print("GAME OVER! I WON!")
            break

        # for ship in player_ships:
        #     print(
        #         f"{ship.name} is_sunk: {ship.is_sunk}, hits: {ship.num_hits}, {ship.coordinates}"
        #     )


#     1  2  3  4  5  6  7  8  9  10
#    ------------------------------
# a | o  o  *  o  o  ·  ·  ·  ·  ·
# b | ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
# c | ·  ·  ·  ·  ·  ·  ·  o  ·  ·
# d | ·  o  ·  ·  ·  ·  ·  o  ·  ·
# e | ·  o  ·  o  o  ·  ·  o  ·  ·
# f | ·  o  ·  ·  ·  ·  ·  o  ·  ·
# g | ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
# h | ·  ·  ·  o  o  o  ·  ·  ·  ·
# i | ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
# j | ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
