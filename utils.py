import json


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

    if stats == 0:  # If this is true, then it will read the value of gold (top_layer).
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
