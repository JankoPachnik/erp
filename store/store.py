""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common
import main



def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    # your code
    options_inventory = ["Show table",
                         "Add",
                         "Remove",
                         "Update",
                         "get counts by manufacturers(",
                         "get average by manufacturer"]

    file_directory = 'store/games.csv'
    table = data_manager.get_table_from_file(file_directory)
    ui.print_menu("Store menu", options_inventory, "Exit program")
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(table)
    elif option == "2":
        add(table)
        data_manager.write_table_to_file(file_directory, table)
    elif option == "3":
        id_ = input('Please provide ID of a record you want to delete\n')
        remove(table, id_)
        data_manager.write_table_to_file(file_directory, table)
    elif option == "4":
        id_ = input('Please provide ID of a record you want to edit\n')
        update(table, id_)
        data_manager.write_table_to_file(file_directory, table)
    elif option == "5":
        get_counts_by_manufacturers(table)
    elif option == "6":
        get_average_by_manufacturer(table, manufacturer)
    elif option == "0":
        main.main()
    else:
        raise KeyError("There is no such option.")


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    # your code


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    try:
        unique_id = common.generate_random(table)
        title = input('Please write a title of a game\n')
        manufacturer = input('Please write a manufacturer\n')
        price = input('Please write a price \n')
        in_stock = input('Please write how many days in stock \n')
        new_row = (unique_id, title, manufacturer, price, in_stock)
        table.append(new_row)
        return table
    except ValueError:
        print('you need to provide correct Values.')

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    try:
        for i in range(len(table)):
            if table[i][0] == id_:
                table.remove(table[i])
    except ValueError:
        print('The ID you are trying to reach is currently unavailable')
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    try:
        for i in range(len(table)):
            if table[i][0] == id_:
                print('Now you can edit data of a file. Leave blank space to keep remaining value\n')
                game_name = input('Update name of the Employee (current: {})\n'.format(table[i][1]))
                manufacturer = input('Update sales price (current: {})\n'.format(table[i][2]))
                price = input('Update month of a sales (current: {})\n'.format(table[i][3]))
                in_stock = input('Update day of a sales (current: {})\n'.format(table[i][4]))
                if game_name != '':
                    table[i][1] = game_name
                if manufacturer != '':
                    table[i][2] = manufacturer
                if price != '':
                    table[i][3] = price
                if in_stock != '':
                    table[i][4] = in_stock
    except ValueError:
        print('The ID you are trying to reach is currently unavailable')
    return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    # your code


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    # your code
