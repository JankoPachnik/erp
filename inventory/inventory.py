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
    module_active = 1
    while module_active == 1:
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
            id_ = ui.get_inputs(['id: '], 'Please provide ID of a record you want to delete')
            remove(table, id_[0])
            data_manager.write_table_to_file(file_directory, table)
        elif option == "4":
            id_ = ui.get_inputs(['Please provide ID of a record you want to edit\n'], "")
            update(table, id_[0])
            data_manager.write_table_to_file(file_directory, table)
        elif option == "5":
            available = get_available_items(table)
            ui.print_result(available, 'These items are available')
        elif option == "6":
            durability = get_average_durability_by_manufacturers(table)
            ui.print_result(durability, 'Average durability by manufacturers')
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
    title_list = ["Id", "Name", "Manufacturer", "Year", "Durability"]
    ui.print_table(table, title_list)


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
        game_data = ui.get_inputs(['Name: ', 'Manufacturer: ', 'Year: ', 'Durability: '],
                                  "Please provide information about product")
        new_row = (unique_id, game_data[0], game_data[1], game_data[2], game_data[3])
        table.append(new_row)
        return table
    except ValueError:
        ui.print_error_message('you need to provide correct Values.')

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
        ui.print_error_message('The ID you are trying to reach is currently unavailable')
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
                game_data = ui.get_inputs(['Name ({}): '.format(table[i][1]), 'Manufaturer ({}): '.format(table[i][2]),
                                           'Year ({}): '.format(table[i][3]), 'Durability ({}): '.format(table[i][4])],
                                          "Please update information about product")
                if game_data[0] != '':
                    table[i][1] = game_data[0]
                if game_data[1] != '':
                    table[i][2] = game_data[1]
                if game_data[2] != '':
                    table[i][3] = game_data[2]
                if game_data[3] != '':
                    table[i][4] = game_data[3]
    except ValueError:
        ui.print_error_message('The ID you are trying to reach is currently unavailable')
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
    no_items = 'No items are available'
    year_and_durability = []
    table_len = len(table)

    for row in range(table_len):
        if (int(table[row][3]) + int(table[row][4]) >= 2017):
            year_and_durability.append(table[row])

    if year_and_durability == None:
        return no_items

    return year_and_durability

def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    # your code
    manufacturers = []
    manufacturers_durability = []
    table_len = len(table)

    manufacturer_avarage_durability = {

    }

    for i in range(table_len):
        manufacturers.append(table[i][2])
        manufacturers_durability.append(table[i][4])

    for j in range(table_len):
        number = 0
        sum_of_durability = 0
        if manufacturers[j] in manufacturer_avarage_durability:
            continue
        for k in range(table_len):
            if manufacturers[k] == manufacturers[j]:
                number += 1
                sum_of_durability += int(manufacturers_durability[k])
        manufacturer_avarage_durability[manufacturers[j]] = sum_of_durability/number
              
    return manufacturer_avarage_durability