""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
"""

# everything you'll need is imported:
# User interface module
import ui
import main
# data manager module
import data_manager
# common module
import common
import datetime
from operator import itemgetter

ID = 0
TITLE = 1
PRICE = 2
MONTH = 3
DAY = 4
YEAR = 5

def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    module_active = 1
    while module_active == 1:
        options_inventory = ["Show table",
                             "Add",
                             "Remove",
                             "Update",
                             "get lowest price item id",
                             "get items old between"]

        file_directory = 'sales/sales.csv'
        table = data_manager.get_table_from_file(file_directory)
        ui.print_menu("Sales menu", options_inventory, "Exit program")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
            data_manager.write_table_to_file(file_directory, table)
        elif option == "3":
            id_ = ui.get_inputs(['Please provide ID of a record you want to delete\n'], "")
            remove(table, id_[0])
            data_manager.write_table_to_file(file_directory, table)
        elif option == "4":
            id_ = ui.get_inputs(['Please provide ID of a record you want to edit\n'], "")
            update(table, id_[0])
            data_manager.write_table_to_file(file_directory, table)
        elif option == "5":
            get_lowest_price_item_id(table)
        elif option == "6":
            get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
        elif option == "0":
            module_active = 0
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

    title_list = ["Id", "Title", "Price", "Month", "Day", "Year"]
    ui.print_table(table, title_list)


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
        game_data = ui.get_inputs(['Game name: ', 'Price: ', 'Month: ', 'Day: ', 'Year: '],
                                  "Please provide information about product")
        new_row = (unique_id, game_data[0], game_data[1], game_data[2], game_data[3], game_data[4])
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
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    try:
        for i in range(len(table)):
            if table[i][0] == id_:
                print('Now you can edit data of a file. Leave blank space to keep remaining value\n')
                game_data = ui.get_inputs(['Game name ({}): '.format(table[i][1]), 'Price ({}): '.format(table[i][2]),
                                           'Month ({}): '.format(table[i][3]), 'Day ({}): '.format(table[i][4]),
                                           'Year ({}): '.format(table[i][5])], "Please update information about product")
                if game_data[0] != '':
                    table[i][1] = game_data[0]
                if game_data[1] != '':
                    table[i][2] = game_data[1]
                if game_data[2] != '':
                    table[i][3] = game_data[2]
                if game_data[3] != '':
                    table[i][4] = game_data[3]
                if game_data[4] != '':
                    table[i][5] = game_data[4]
    except ValueError:
        print('The ID you are trying to reach is currently unavailable')
    return table


# special functions:
# ------------------

def get_lowest_price_item_id(table):

    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list of lists): data table to work on

    Returns:
         string: id
    """
    min_price = int(table[0][PRICE])
    for row in table:
        current_price = int(row[PRICE])
        if current_price < min_price:
            min_price = current_price
    rows_with_lowest_price = []
    for row in table:
        if int(row[PRICE]) == min_price:
            rows_with_lowest_price.append(row)
    
    sorted_list = sorted(rows_with_lowest_price, key=itemgetter(TITLE))
    print (sorted_list)


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """
   
   






    # your code
