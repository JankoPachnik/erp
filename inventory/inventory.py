""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
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
                         "Available items",
                         "Average durability"]
    file_directory = 'inventory/inventory.csv'
    table = data_manager.get_table_from_file(file_directory)
    ui.print_menu("Inventory Menu", options_inventory, "Exit program")
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
    print(table)
    # ui.print_table(table)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code 4444
    try:
        unique_id = common.generate_random(table)
        console = input('Please write a name of a console you want to add\n')
        developer = input('Please write a name of developer\n')
        year = input('Please write a year the game was published\n')
        stock = input('Please write number of copies you want to add\n')
        new_row = (unique_id, console, developer, year, stock)
        table.append(new_row)
        return table
    except ValueError:
        print('you need to provide correct Values.')


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
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    try:
        for i in range(len(table)):
            if table[i][0] == id_:
                print('Now you can edit data of a file. Leave blank space to keep remaining value\n')
                console = input('Update name of a Console (current: {})\n'.format(table[i][1]))
                developer = input('Update name of a developer (current: {})\n'.format(table[i][2]))
                year = input('Update date of release (current: {})\n'.format(table[i][3]))
                stock = input('Update number of copies (current: {})\n'.format(table[i][4]))
                if console != '':
                    table[i][1] = game_name
                if developer != '':
                    table[i][2] = developer
                if year != '':
                    table[i][3] = year
                if stock != '':
                    table[i][4] = stock
    except ValueError:
        print('The ID you are trying to reach is currently unavailable')
    return table


# special functions:
# ------------------

def get_available_items(table):
    """
    Question: Which items have not exceeded their durability yet?

    Args:
        table (list): data table to work on

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    # your code


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    # your code
