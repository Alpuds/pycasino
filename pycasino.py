"""
Pycasino is a casino in which it uses gold as currency. Gold can be obtained through playing games such as blackjack, slots, and more.
Of course, in order to play said games, gold needs to be put in as the bet. In addition, stats for each game is available.
This consists of times played, total win/loss and net gain of gold.
"""
import json

from games.blackjack import blackjack
from games.craps import craps
from games.roulette import roulette
from games.slots import slots

games = {"bj": blackjack, "blackjack": blackjack, "slots": slots, "roulette": roulette, "craps": craps}

# def title():
#     print("██████╗ ██╗   ██╗ ██████╗ █████╗ ███████╗██╗███╗   ██╗ ██████╗".center(98, "-"))
#     print("██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗██╔════╝██║████╗  ██║██╔═══██╗".center(100, "-"))
#     print("██████╔╝ ╚████╔╝ ██║     ███████║███████╗██║██╔██╗ ██║██║   ██║".center(100, "-"))
#     print("██╔═══╝   ╚██╔╝  ██║     ██╔══██║╚════██║██║██║╚██╗██║██║   ██║".center(100, "-"))
#     print("██║        ██║   ╚██████╗██║  ██║███████║██║██║ ╚████║╚██████╔╝".center(100, "-"))
#     print("╚═╝        ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝".center(98, "-"))


def list_of_commands():
    with open("help.txt", "r") as f:
        return f.read()


def print_all_stats(game):
    """Prints out all of the stats for the chosen game"""
    get_value = lambda stats: read_data(game, stats)
    print(f"Stats for {game}:")
    print(f"Wins: {get_value('wins'):,}")
    print(f"Losses: {get_value('losses'):,}")
    print(f"Total gold won: {get_value('total gold won'):,}")
    print(f"Total gold lost: {get_value('total gold lost'):,}")
    print(f"Gold net amount: {get_value('gold net amount'):,}")


def read_data(top_layer, stats=0):
    """
    Reads data.json and returns the number of gold or statistic of a game.
    top_layer refers to the key that is at the top of the hierarchy (e.g., gold, blackjack).
    stats is one statistic from a game (e.g., wins statistic from blackjack).
    """
    with open("data.json", "r") as file:
        data = json.load(file)

    if stats == 0: # If this is true, then it will read the value of gold (top_layer).
        return data[top_layer]
    else:
        # Read the value of stats for a game (which top_layer represents).
        return data[top_layer][stats]


def write_data(top_layer, stats, value=0):
    """
    Writes data to data.json. It can update gold or a game's specific statistic (e.g., wins).

    If 2 arguments are given, then it will assign the value of stats to be the value of the key, top_layer.
    Main use of this is to do write_data("gold", 5) to make the value of gold be 5.

    If 3 arguments are given, then it will write the value of the stats for the given game.
    E.g., write_data("blackjack", "wins", 10) will write 10 for wins for blackjack in data.json.
    """
    with open("data.json", "r") as file:
        data = json.load(file)

    if value == 0:
        data["gold"] = stats
    else:
        data[top_layer][stats] = value

    # Write changes to data.json
    with open("data.json", "w") as write_file:
        json.dump(data, write_file, indent=4)


def abbrv(num):
    """
    Shortens the amount so it will have a letter at the end to indicate the place value of the number (e.g. 1,500 -> 1.5K)
    This goes upto trillion.
    """
    abbrv = {"T": 1_000_000_000_000, "B": 1_000_000_000, "M": 1_000_000, "K": 1000}
    for key, abbrv_value in abbrv.items():
        if num / abbrv_value >= 1:
            shorten_num = str(round((num / abbrv_value), 2)).strip(".0")
            return shorten_num + key


def expand(num):
    """Expands the abbreviation of a number (e.g. 1.5K -> 1,500)"""
    abbrv = {"T": 1_000_000_000_000, "B": 1_000_000_000, "M": 1_000_000, "K": 1000}
    # Stores the letter that is at the end of the number to match the key and be the multiplyer
    abbrv_letter = num[-1]
    num = float(num.strip(abbrv_letter))
    # This will ensure the letter is capitalised to match the key
    abbrv_letter = abbrv_letter.upper()
    return int(num * abbrv[abbrv_letter])


def check_abbrv(num):
    """
    Checks to see if the number is abbreviated.
    Returns True if the number is abbreviated and False if it is not.
    """
    try:
        int(num)
        return False
    except ValueError:
        letter = num[-1].upper()
        abbrv = ("T", "B", "M", "K")
        if letter in abbrv:
            return True
        else:
            return "invalid"


if __name__ == "__main__":
    gold = read_data("gold")

    while True:
        try:
            command = input("Command: ")
            command, bet = command.split()
            # ---Stats----#
            if command == "stats":
                if bet in games:
                    # Make bet be blackjack to match with the name in data.json
                    if bet == "bj":
                        bet = "blackjack"
                    print_all_stats(bet)
                else:
                    print(
                        f'The game "{bet}" is not available. Type "h" or "help" to see a list of commands'
                    )
            # ------------#
            elif command in games:
                # ---Checks the integrity of the bet and expands it when needed---#
                if check_abbrv(bet) == True:
                    bet = expand(bet)
                elif check_abbrv(bet) == "invalid":
                    print(
                        f"{bet} is invalid. Pycasino only handles numbers that are under one quadrillion"
                    )
                    continue
                else:
                    bet = int(bet)
                if bet > gold:
                    print(f"You don't have enough gold ({abbrv(gold)}) [{gold:,}].")
                    continue
                elif bet <= 0:
                    print("You have to bet an amount greater than 0.")
                    continue
                # ----------------------------------------------------------------#
                # ---Game---#
                games[command](bet)
                continue
                # ----------#
            # --Add gold when allowed---#
            elif command == "add" and bet == "gold":
                if gold == 0:
                    write_data("gold", 100)
                    gold = read_data("gold")
                    print("Added 100 gold.")
                else:
                    print("You can only add gold if you ran out of it.")
            # --------------------------#
            else:
                print('Invalid command. Type "h" or "help" for a list of commands')
                continue

        except ValueError:
            if command == "gold":
                print(
                    f"You have {gold:,} ({abbrv(gold)}) gold."
                    if gold > 1000
                    else f"You have {gold} gold."
                )

            elif command == "q" or command == "Q":
                break

            elif command == "h" or command == "help":
                print(list_of_commands())

            # ---Zero argument error handling---#
            elif command in games:
                print("You need to provide a bet.")

            elif command == "stats":
                print("You need to provide a game to get stats.")

            elif command == "add":
                print(
                    'Type "add gold" to receive 100 gold if and only if you ran out of gold.'
                )
            # ----------------------------------#
            else:
                print('Invalid command. Type "h" or "help" for a list of commands')
                continue
