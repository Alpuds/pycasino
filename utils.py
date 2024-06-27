import json


def help_text():
    """Returns the help text."""
    with open("help.txt", "r") as f:
        return f.read()


def print_all_stats(game: str):
    """
    Prints out all of the stats for GAME.

    Parameters
    game: The game to print stats of.
    """
    get_value = lambda stats: read_data(game, stats)
    print(f"Stats for {game}:")
    print(f"Wins: {get_value('wins'):,}")
    print(f"Losses: {get_value('losses'):,}")
    print(f"Total gold won: {get_value('total gold won'):,}")
    print(f"Total gold lost: {get_value('total gold lost'):,}")
    print(f"Gold net amount: {get_value('gold net amount'):,}")


def read_data(top_layer: str, stats: str = "") -> int:
    """
    Reads data.json and returns the number of gold or statistic of a game.

    Parameters
    top_layer: The key that is at the top of the hierarchy (e.g., gold, blackjack).
    stats: A statistic from a game (e.g., wins statistic from blackjack).

    Returns
    The number of gold if 1 argument is given.
    The statistic of a game if 2 arguments are given.
    """
    with open("data.json", "r") as file:
        data = json.load(file)

    if stats == "":  # If this is true, then it will read the value of gold (top_layer).
        return data[top_layer]
    else:
        # Read the value of stats for a game (which top_layer represents).
        return data[top_layer][stats]


def write_data(top_layer: str, stats: int | str, value: int = 0):
    """
    Writes data to data.json.
    It can update gold and a game's specific statistic (e.g., wins).

    If 2 arguments are given, then it will assign the value of STATS
    to be the value of the key, TOP_LAYER.
    Main use of this is to do write_data("gold", 5) to assign the value of gold to be 5.

    If 3 arguments are given, then it will write VALUE
    for STATS for the given game (TOP_LAYER).
    E.g., write_data("blackjack", "wins", 10) will write 10 for wins in blackjack.

    Parameters
    top_layer: The key that is at the top of the hierarchy (e.g., gold, blackjack).
    stats: The amount of gold to write (int) OR a game statistic to update (str).
    value: A number to write for a game statistic.
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


def abbrv(num: int) -> str | int:
    """
    Abbreviates NUM to 1 decimal place followed by the appropriate unit (K, M, B...).
    If NUM is less than 1,000, then the number will be returned as is.
    The max unit is a trillion (T).

    Parameters
    num: The number to abbreviate.

    Returns
    A string that contains a number to the first decimal place followed by a unit.
    (E.g., abbrv(1_500) -> '1.5K')
    NUM if NUM < 1000
    """
    abbrv = {"T": 1_000_000_000_000, "B": 1_000_000_000, "M": 1_000_000, "K": 1000}
    for key, abbrv_value in abbrv.items():
        if num / abbrv_value >= 1:
            shorten_num = str(round((num / abbrv_value), 2)).strip(".0")
            return shorten_num + key
    return num


def expand(num: str) -> int:
    """
    Returns an abbreviated number as an integer.
    (E.g., expand('1.5K') -> 1500)

    Parameters
    num: An abbreviated number.
    """
    abbrv = {"T": 1_000_000_000_000, "B": 1_000_000_000, "M": 1_000_000, "K": 1000}
    # Stores the letter that is at the end of the number to match the key and be the multiplyer
    abbrv_letter = num[-1]
    float_num = float(num.strip(abbrv_letter))
    # This will ensure the letter is capitalised to match the key
    abbrv_letter = abbrv_letter.upper()
    return int(float_num * abbrv[abbrv_letter])


def check_abbrv(num: str) -> bool | str:
    """
    Checks if NUM is abbreviated.

    Parameters
    num: A string that contains a number

    Returns
    True if NUM is abbreviated with a valid unit (unit <= T).
    False if NUM is not abbreviated.
    "invalid" if NUM contains an invalid abbreviation (unit > T).
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
