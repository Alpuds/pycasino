"""
Pycasino is a casino in which it uses gold as currency. Gold can be obtained through playing games such as blackjack, slots, and more.
Of course, in order to play said games, gold needs to be put in as the bet. In addition, stats for each game is available.
This consists of times played, total win/loss and net gain of gold.
"""
import csv

from games import blackjack as bj

def title():
    print("██████╗ ██╗   ██╗ ██████╗ █████╗ ███████╗██╗███╗   ██╗ ██████╗".center(98, "-"))
    print("██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗██╔════╝██║████╗  ██║██╔═══██╗".center(100, "-"))
    print("██████╔╝ ╚████╔╝ ██║     ███████║███████╗██║██╔██╗ ██║██║   ██║".center(100, "-"))
    print("██╔═══╝   ╚██╔╝  ██║     ██╔══██║╚════██║██║██║╚██╗██║██║   ██║".center(100, "-"))
    print("██║        ██║   ╚██████╗██║  ██║███████║██║██║ ╚████║╚██████╔╝".center(100, "-"))
    print("╚═╝        ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝".center(98, "-"))

<<<<<<< HEAD
gold = 1_665_390
=======
username = "Alpud"
data_path = "./users/" + username + "/data.csv"
>>>>>>> user_csv_handling

def list_of_commands():
    with open("help.txt", "r") as f:
       return f.read()

<<<<<<< HEAD
=======
def read_data(field):
    with open(data_path, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            return line[field]

>>>>>>> user_csv_handling
def abbrv(num):
    """Shortens the amount so it will have a letter at the end to indicate the place value of the number (e.g. 1.5K = 1,500)
       This goes upto trillion.
    """
    abbrv = {"T": 1_000_000_000_000, "B": 1_000_000_000, "M": 1_000_000, "K": 1_000}
    for abbrv_value in abbrv.values():
        if num / abbrv_value >= 1:
            shorten_num = str(round((num / abbrv_value), 2)).strip(".0")
            for key, value in abbrv.items():
                if value == abbrv_value:
                    return shorten_num + key

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
<<<<<<< HEAD
            print(f"You have {gold:,} ({abbrv(gold)}) gold.")
=======
            gold = int(read_data("gold"))
            print(f"You have {gold:,} ({abbrv(gold)}) gold." if gold > 1_000 else f"You have {gold} gold.")
>>>>>>> user_csv_handling

        elif command == "q" or command == "Q":
            break

        else:
            print(list_of_commands())
            continue
