"""
Pycasino is a casino in which it uses gold as currency. Gold can be obtained through playing games such as blackjack, slots, and more.
Of course, in order to play said games, gold needs to be put in as the bet. In addition, stats for each game is available.
This consists of times played, total win/loss and net gain of gold.
"""
import csv

from games import blackjack as bj

# def title():
#     print("██████╗ ██╗   ██╗ ██████╗ █████╗ ███████╗██╗███╗   ██╗ ██████╗".center(98, "-"))
#     print("██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗██╔════╝██║████╗  ██║██╔═══██╗".center(100, "-"))
#     print("██████╔╝ ╚████╔╝ ██║     ███████║███████╗██║██╔██╗ ██║██║   ██║".center(100, "-"))
#     print("██╔═══╝   ╚██╔╝  ██║     ██╔══██║╚════██║██║██║╚██╗██║██║   ██║".center(100, "-"))
#     print("██║        ██║   ╚██████╗██║  ██║███████║██║██║ ╚████║╚██████╔╝".center(100, "-"))
#     print("╚═╝        ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝".center(98, "-"))

username = "Alpud"
data_path = "./users/" + username + "/data.csv"


def list_of_commands():
    with open("help.txt", "r") as f:
        return f.read()


def print_all_stats(game):
    """Prints out all of the stats for the chosen game"""
    print(f"Stats for {game}:")
    print(f"Wins: {read_data('game', game, 'wins')}")
    print(f"Losses: {read_data('game', game, 'losses')}")
    print(f"Total gold gained: {read_data('game', game, 'total gold gained')}")
    print(f"Total gold lost: {read_data('game', game, 'total gold lost')}")
    print(f"Gold net value: {read_data('game', game, 'gold net value')}")


def read_data(field, game=0, stats=0):
    """
    Reads the data.csv file from the current user's folder.
    It can be used to get the number of gold or statistic of a game
    """
    with open(data_path, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        if game == 0:
            for line in csv_reader:
                return int(line[field])
        else:
            for line in csv_reader:
                if line[field] == game:
                    return int(line[stats])


def abbrv(num):
    """
    Shortens the amount so it will have a letter at the end to indicate the place value of the number (e.g. 1.5K = 1,500)
    This goes upto trillion.
    """
    abbrv = {"T": 1_000_000_000_000, "B": 1_000_000_000, "M": 1_000_000, "K": 1000}
    for abbrv_value in abbrv.values():
        if num / abbrv_value >= 1:
            shorten_num = str(round((num / abbrv_value), 2)).strip(".0")
            for key, value in abbrv.items():
                if value == abbrv_value:
                    return shorten_num + key


while True:
    try:
        command = input("Command: ")
        command, bet = command.split()
        if command == "bj":
            bj.blackjack(bet)
            continue
        elif command == "stats":
            if bet == "bj":
                print_all_stats("blackjack")
            elif bet == "slots":
                print_all_stats("slots")
            elif bet == "roulette":
                print_all_stats("roulette")
            else:
                print(
                    f'{bet.capitalize()} is not a game available. Type "h" or "help" to see a list of commands'
                )
        else:
            print('Invalid command. Type "h" or "help" for a list of commands')
            continue

    except ValueError:
        if command == "gold":
            gold = read_data("gold")
            print(
                f"You have {gold:,} ({abbrv(gold)}) gold."
                if gold > 1000
                else f"You have {gold} gold."
            )

        elif command == "q" or command == "Q":
            break

        elif command == "h" or command == "help":
            print(list_of_commands())

        else:
            print('Invalid command. Type "h" or "help" for a list of commands')
            continue
