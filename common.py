""" Common module
implement commonly used functions here
"""
import random
import string


def get_random_digit():
    x = random.choice(string.digits)
    return x


def get_random_lower():
    x = random.choice(string.ascii_lowercase)
    return x


def get_random_upper():
    x = random.choice(string.ascii_uppercase)
    return x


def get_random_special():
    x = ';'
    while x == ';':
        x = random.choice(string.punctuation)
    return x


# generates random number
def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """
    table_directory = table + '/' + table + '.csv'
    id_in_file = []
    with open(table_directory, 'r') as f:
        for line in f:
            id_in_file.append(line[:8].strip())
    generated = (get_random_lower() + get_random_special() +
                 get_random_digit() + get_random_upper() +
                 get_random_special() + get_random_upper() +
                 get_random_lower() + get_random_digit())
    return generated



