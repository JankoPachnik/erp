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

TYPE = 4


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
            id_ = ui.get_inputs(['Please provide ID of a record you want to delete\n'], "")
            remove(table, id_[0])
            data_manager.write_table_to_file(file_directory, table)
        elif option == "4":
            id_ = ui.get_inputs(['Please provide ID of a record you want to edit\n'], "")
            update(table, id_[0])
            data_manager.write_table_to_file(file_directory, table)
        elif option == "5":
            max_year = which_year_max(table)
            ui.print_result(max_year[0], max_year[1])
        elif option == "6":
            year = ui.get_inputs(['year: \n'], "Please provide year you want to check ")
            avg_profit = avg_amount(table, year)
            label = 'The average profit in year ' + str(year)
            ui.print_result(avg_profit, label)
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
        ui.print_error_message('The ID you are trying to reach is currently unavailable')
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
    d = {}
    for i in range(len(table)):
        if table[i][TYPE] == 'in':
            d[table[i][3]] = int(table[i][5]) + d.setdefault(table[i][3], 0)
        if table[i][TYPE] == 'out':
            d[table[i][3]] = d.setdefault(table[i][3], 0) - int(table[i][5])
    max_year = ['', -99999999999]
    for key, value in d.items():
        if value >= max_year[1]:
            max_year[0] = key
            max_year[1] = value
    return max_year


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """
    year_list = []
    for i in range(len(table)):
        if table[i][3] == year[0]:
            if table[i][4] == 'in':
                year_list.append(int(table[i][5]))
            if table[i][4] == 'out':
                year_list.append(int(table[i][5])*-1)
    profit = 0
    for i in range(len(year_list)):
        profit += year_list[i]
    avg_profit = profit / len(year_list)
    return avg_profit

