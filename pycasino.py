"""
Pycasino is a casino in which it uses gold as currency. Gold can be obtained through playing games such as blackjack, slots, and more.
Of course, in order to play said games, gold needs to be put in as the bet. In addition, stats for each game is available.
This consists of times played, total win/loss and net gain of gold.
"""
import csv
import os

from games.blackjack import blackjack
from games.craps import craps
from games.roulette import roulette
from games.slots import slots

games = {"bj": blackjack, "slots": slots, "roulette": roulette, "craps": craps}

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
    get_value = lambda field: read_data('game', game, field)
    print(f"Stats for {game}:")
    print(f"Wins: {get_value('wins'):,}")
    print(f"Losses: {get_value('losses'):,}")
    print(f"Total gold gained: {get_value('total gold gained'):,}")
    print(f"Total gold lost: {get_value('total gold lost'):,}")
    print(f"Gold net value: {get_value('gold net value'):,}")


def read_data(field, game=0, stats=0):
    """
    Reads the data.csv file to get the number of gold or statistic of a game
    """
    with open("data.csv", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        if game == 0:
            for line in csv_reader:
                return int(line[field])
        else:
            for line in csv_reader:
                if line[field] == game:
                    return int(line[stats])


def write_data(field, write, game=0, stat=0):
    """
    Writes data to the data.csv. It can update gold or a game's specific statistic (e.g. wins).
    """
    with open('data.csv', 'r') as csv_file, open('updated_data.csv', 'w') as f:
        field_names = ('gold', 'game', 'wins', 'losses', 'total gold gained', 'total gold lost', 'gold net value')

        csv_writer = csv.DictWriter(f, fieldnames=field_names)
        csv_reader = csv.DictReader(csv_file)

        csv_writer.writeheader()

        for line in csv_reader:
            if game != 0:
                if line[field] == game:
                    line[stat] = write
            # Relies on "gold" being the first field name
            elif line[field] != write and line[field] != 'x':
                line[field] = write
            else:
                line[field] = 'x'
            # Updates data
            row = {'gold': line['gold'], 'game': line['game'], 'wins': line['wins'], 'losses': line['losses'],'total gold gained': line['total gold gained'], 'total gold lost': line['total gold lost'], 'gold net value': line['gold net value'] }
            csv_writer.writerow(row)

        os.rename('updated_data.csv', 'data.csv')


def abbrv(num):
    """
    Shortens the amount so it will have a letter at the end to indicate the place value of the number (e.g. 1,500 -> 1.5K)
    This goes upto trillion.
    """
    abbrv = {"T": 1_000_000_000_000, "B": 1_000_000_000, "M": 1_000_000, "K": 1000}
    for abbrv_value in abbrv.values():
        if num / abbrv_value >= 1:
            shorten_num = str(round((num / abbrv_value), 2)).strip(".0")
            for key, value in abbrv.items():
                if value == abbrv_value:
                    return shorten_num + key


def expand(num):
    """Expands the abbreviation of a number (e.g. 1.5K -> 1,500)"""
    abbrv = {"T": 1_000_000_000_000, "B": 1_000_000_000, "M": 1_000_000, "K": 1000}
    # Stores the letter that is at the end of the number to match the key and be the multiplyer
    abbrv_letter = num[- 1]
    num = float(num.strip(abbrv_letter))
    # This will ensure the letter is capitalised to match the key
    abbrv_letter = abbrv_letter.upper()
    return int(num * abbrv[abbrv_letter])


def check_abbrv(num):
    try:
        int(num)
        return False
    except ValueError:
        letter = num[- 1].upper()
        abbrv = ("T", "B", "M", "K")
        if letter in abbrv:
            return True
        else:
            return "invalid"

if __name__ == '__main__':
    gold = read_data("gold")


    while True:
        try:
            command = input("Command: ")
            command, bet = command.split()
            #---Stats----#
            if command == "stats":
                if bet in games:
                    if bet == "bj":
                        bet = "blackjack"
                    print_all_stats(bet)
                else:
                    print(
                        f'{bet.capitalize()} is not a game available. Type "h" or "help" to see a list of commands'
                    )
            #------------#
            elif command in games:
                #---Checks the integrity of the bet and expands it when needed---#
                if check_abbrv(bet) == True:
                    bet = expand(bet)
                elif check_abbrv(bet) == "invalid":
                    print("Pycasino only handles numbers that are under one quadrillion")
                    continue
                else:
                    bet = int(bet)
                #----------------------------------------------------------------#
                if bet > gold:
                    print(f"You don't have enough gold. [{gold:,}] ({abbrv(gold)})")
                    continue
                #---Game---#
                games[command](bet)
                continue
                #----------#
            #--Add gold when allowed---#
            elif command == 'add' and bet == 'gold':
                if gold == 0:
                    write_data('gold', 100)
                    print('Added 100 gold.')
                else:
                    print('You can only add gold if you ran out of it.')
            #--------------------------#
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

            #---Zero argument error handling---#
            elif command in games:
                 print("You need to provide a bet.")

            elif command == "stats":
                print("You need to provide a game to get stats.")

            elif command == "add":
                print('Type "add gold" to receive 100 gold if and only if you ran out of gold.')
            #----------------------------------#
            else:
                print('Invalid command. Type "h" or "help" for a list of commands')
                continue
