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
    module_active = 1
    while module_active == 1:
        labels_count=['Manufacturer', 'Number']
        labels_avarage=['Avarege items available in stock by given manufacturer']
        options_inventory = ["Show table",
                             "Add",
                             "Remove",
                             "Update",
                             "Get counts by manufacturers",
                             "Get average by manufacturer"]

        file_directory = "store/games.csv"
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
            id_ = ui.get_inputs(['id: '], 'Please provide ID of a record you want to delete')
            remove(table, id_)
            data_manager.write_table_to_file(file_directory, table)
        elif option == "4":
            id_ = ui.get_inputs(['Please provide ID of a record you want to edit\n'], "")
            update(table, id_[0])
            data_manager.write_table_to_file(file_directory, table)
        elif option == "5":
            manufacturer = get_counts_by_manufacturers(table)
            ui.print_result(manufacturer, labels_count)
        elif option == "6":
            manufacturer = ui.get_inputs(['Manufacturer: '], 'Please provide Manufacturer that you want to count')
            available = get_average_by_manufacturer(table, manufacturer)
            ui.print_result(available, labels_avarage)
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
    title_list = ["Id", "Gra", "Producent", "Liczba1", "Liczba2"]
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
        game_data = ui.get_inputs(['Game name: ', 'Manufacturer: ', 'Price: ', 'Days in stock: '],
                                  "Please provide information about product")
        new_row = (unique_id, game_data[0], game_data[1], game_data[2], game_data[3])
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
        ui.print_error_message('The ID you are trying to reach is currently unavailable')
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
                game_data = ui.get_inputs(['Game name ({}): '.format(table[i][1]), 'Price ({}): '.format(table[i][2]),
                                           'Month ({}): '.format(table[i][3]), 'Day ({}): '.format(table[i][4]),
                                           ], "Please update information about product")
                if game_data[0] != '':
                    table[i][1] = game_data[0]
                if game_data[1] != '':
                    table[i][2] = game_data[1]
                if game_data[2] != '':
                    table[i][3] = game_data[2]
                if game_data[3] != '':
                    table[i][4] = game_data[3]

    except ValueError:
        print('The ID you are trying to reach is currently unavailable')
    return table


# special functions:
# ------------------
#ggg

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    # your code
    manufacturers = [] 
    manucount = {
    }

    table_len = len(table)
    for i in range(table_len):
        manufacturers.append(table[i][2])
    manu_len = len(manufacturers)
    for i in range(manu_len):
        number = 0
        if manufacturers[i] in manucount:
            continue
        for j in range(manu_len):
            if manufacturers[j] == manufacturers[i]:
                number += 1            
        manucount[manufacturers[i]] = number
    return manucount


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
    manufacturers = [] 
    manufacturers_stock = []
    stock_number = 0
    table_len = len(table)
    number = 0

    for i in range(table_len):
        manufacturers.append([table[i][2]])
        manufacturers_stock.append(table[i][4])

    for i in range(table_len):
        if manufacturer == manufacturers[i]:
            stock_number += float(manufacturers_stock[i])
            number += 1

    average = stock_number/number

    return average
