"""
Pycasino is a casino in which it uses gold as currency. Gold can be obtained through playing games such as blackjack, slots, and more.
Of course, in order to play said games, gold needs to be put in as the bet. In addition, stats for each game is available.
This consists of times played, total win/loss and net gain of gold.
"""

from games.blackjack import blackjack
from games.craps import craps
from games.roulette import roulette
from games.slots import slots
import utils

games = {
    "bj": blackjack,
    "blackjack": blackjack,
    "slots": slots,
    "roulette": roulette,
    "craps": craps,
}

# def title():
#     print("██████╗ ██╗   ██╗ ██████╗ █████╗ ███████╗██╗███╗   ██╗ ██████╗".center(98, "-"))
#     print("██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗██╔════╝██║████╗  ██║██╔═══██╗".center(100, "-"))
#     print("██████╔╝ ╚████╔╝ ██║     ███████║███████╗██║██╔██╗ ██║██║   ██║".center(100, "-"))
#     print("██╔═══╝   ╚██╔╝  ██║     ██╔══██║╚════██║██║██║╚██╗██║██║   ██║".center(100, "-"))
#     print("██║        ██║   ╚██████╗██║  ██║███████║██║██║ ╚████║╚██████╔╝".center(100, "-"))
#     print("╚═╝        ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝".center(98, "-"))


gold = utils.read_data("gold")

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
                utils.print_all_stats(bet)
            else:
                print(
                    f'The game "{bet}" is not available. Type "h" or "help" to see a list of commands'
                )
        # ------------#
        elif command in games:
            # ---Checks the integrity of the bet and expands it when needed---#
            if utils.check_abbrv(bet) == True:
                bet = utils.expand(bet)
            elif utils.check_abbrv(bet) == "invalid":
                print(
                    f"{bet} is invalid. Pycasino only handles numbers that are under one quadrillion"
                )
                continue
            else:
                bet = int(bet)
            if bet > gold:
                print(f"You don't have enough gold ({utils.abbrv(gold)}) [{gold:,}].")
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
                utils.write_data("gold", 100)
                gold = utils.read_data("gold")
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
                f"You have {gold:,} ({utils.abbrv(gold)}) gold."
                if gold > 1000
                else f"You have {gold} gold."
            )

        elif command == "q" or command == "Q":
            break

        elif command == "h" or command == "help":
            print(utils.list_of_commands())

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
