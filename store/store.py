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
        id_ = ui.get_inputs(['id: '], 'Please provide ID of a record you want to edit')
        update(table, id_)
        data_manager.write_table_to_file(file_directory, table)
    elif option == "5":
        manufacturer = get_counts_by_manufacturers(table)
        ui.print_result(manufacturer, labels_count)
    elif option == "6":
        manufacturer = ui.get_inputs(['Manufacturer: '], 'Please provide Manufacturer that you want to count')
        get_average_by_manufacturer(table, manufacturer)
        ui.print_result(manufacturer, labels_avarage)
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
        title = ui.get_inputs(['Title'], 'Please write a title of a game')
        manufacturer = ui.get_inputs(['Manufacturer'], 'Please write a manufacturer')
        price = ui.get_inputs(['Price'], 'Please write a price')
        in_stock = ui.get_inputs(['In Stock'], 'Please write how many days in stock')
        new_row = (unique_id, title, manufacturer, price, in_stock)
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
    avarage = 0
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

    avarage = stock_number/number
    print (avarage)

    return avarage
