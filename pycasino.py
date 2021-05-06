"""
Pycasino is a casino in which it uses gold as currency. Gold can be obtained through playing games such as blackjack, slots, and more.
Of course, in order to play said games, gold needs to be put in as the bet. In addition, stats for each game is available.
This consists of times played, total win/loss and net gain of gold.
"""
from games import blackjack as bj

def title():
    print("██████╗ ██╗   ██╗ ██████╗ █████╗ ███████╗██╗███╗   ██╗ ██████╗".center(98, "-"))
    print("██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗██╔════╝██║████╗  ██║██╔═══██╗".center(100, "-"))
    print("██████╔╝ ╚████╔╝ ██║     ███████║███████╗██║██╔██╗ ██║██║   ██║".center(100, "-"))
    print("██╔═══╝   ╚██╔╝  ██║     ██╔══██║╚════██║██║██║╚██╗██║██║   ██║".center(100, "-"))
    print("██║        ██║   ╚██████╗██║  ██║███████║██║██║ ╚████║╚██████╔╝".center(100, "-"))
    print("╚═╝        ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝".center(98, "-"))

gold = 2593

def list_of_commands():
    with open("help.txt", "r") as f:
       return f.read()

def abbrv_num(amount):
    """Shortens the amount so it will have a letter at the end to indicate the place value of the number (e.g. 1.5K = 1,500)
       This goes upto trillion.
    """

    if amount > 999_999_999_999:
        abbrv = round(amount / 1_000_000_000_000, 2)
        return str(abbrv) + "T"

    elif amount > 999_999_999:
        abbrv = round(amount / 1_000_000_000, 2)
        return str(abbrv) + "B"
    
    elif amount > 999_999:
        abbrv = round(amount / 1_000_000, 2)
        return str(abbrv) + "M"

    else:
        abbrv = round(amount / 1000, 2)
        return str(abbrv) + "K"

while True:
    try:
        command = input("Command: ")
        game, bet = command.split()
        if game == "bj":
            bj.blackjack(bet)
            continue
        else:
            print("Invalid command.")
            print(list_of_commands())
            continue

    except ValueError:
        if command == "gold":
            print(f"You have {gold:,} ({abbrv_num(gold)}) gold.")

        elif command == "q" or command == "Q":
            break

        else:
            print(list_of_commands())
            continue