""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

# everything you'll need is imported:
# User interface module
import ui
import main

# data manager module
import data_manager
# common module
import common


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
                             "which year max",
                             "avg_amount"]

        file_directory = 'accounting/items.csv'
        table = data_manager.get_table_from_file(file_directory)
        ui.print_menu("Accounting menu", options_inventory, "Exit program")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
            data_manager.write_table_to_file(file_directory, table)
        elif option == "3":
            id_ = ui.get_inputs(['Please provide ID of a record you want to delete\n'])
            remove(table, id_)
            data_manager.write_table_to_file(file_directory, table)
        elif option == "4":
            id_ = ui.get_inputs(['Please provide ID of a record you want to edit\n'])
            update(table, id_)
            data_manager.write_table_to_file(file_directory, table)
        elif option == "5":
            get_lowest_price_item_id(table)
        elif option == "6":
            get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
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

    title_list = ["id", "month", "day", "year", "type", "amount"]
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
        game_data = ui.get_inputs(['Month: ', 'Day: ', 'Year: ', 'Type: ', 'Amount: '],
                                  "Please provide information about transaction")
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
                game_data = ui.get_inputs(['Month ({}): '.format(table[i][1]), 'Day ({}): '.format(table[i][2]),
                                           'Year ({}): '.format(table[i][3]), 'Type ({}): '.format(table[i][4]),
                                           'Amount ({}): '.format(table[i][5])],
                                          "Please update information about product")
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

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """

    # your code


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    # your code 4a
