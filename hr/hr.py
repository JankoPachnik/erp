""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
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
                             "Get oldest person",
                             "Get persons closest to average"]

        file_directory = 'hr/persons.csv'
        table = data_manager.get_table_from_file(file_directory)
        ui.print_menu("HR menu", options_inventory, "Exit program")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
            data_manager.write_table_to_file(file_directory, table)
        elif option == "3":
            id_ = ui.get_inputs(['ID: '], 'Please provide ID of a record you want to delete')
            remove(table, id_[0])
            data_manager.write_table_to_file(file_directory, table)
        elif option == "4":
            id_ = ui.get_inputs(['ID: '], 'Please provide ID of a record you want to edit')
            update(table, id_[0])
            data_manager.write_table_to_file(file_directory, table)
        elif option == "5":
            oldest = get_oldest_person(table)
            ui.print_result(oldest, 'Oldest persons: ')
        elif option == "6":
            avarage = get_persons_closest_to_average(table)
            ui.print_result(avarage, 'People closest to average: ')
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
    title_list = ["id", "name", "birth_year"]
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
        game_data = ui.get_inputs(['Name: ', 'Year of birth: '],
                                  "Please provide information about employee")
        new_row = (unique_id, game_data[0], game_data[1])
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
                                           ],"Please update information about product")
                if game_data[0] != '':
                    table[i][1] = game_data[0]
                if game_data[1] != '':
                    table[i][2] = game_data[1]
    except ValueError:
        ui.print_error_message('The ID you are trying to reach is currently unavailable')
    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    # your code
    persons_and_age = table.copy()
    oldest = int(table[0][2])
    oldest_persons = []
    table_len = len(table)

    for rows in range(table_len):
        if int(persons_and_age[rows][2]) < oldest:
            oldest = int(persons_and_age[rows][2])

    for i in range(table_len):
        if int(persons_and_age[i][2]) == oldest:
            oldest_persons.append(persons_and_age[i])

    return oldest_persons


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """    
    # your code

    table_len = len(table)
    avg = 0
    age_sum = 0
    closest_number = 0
    closest_to_avarage = []
    peoples_age = []

    for i in range(table_len):
        peoples_age.append(table[i][2])
        age_sum += int(table[i][2])

    avg = age_sum/table_len
    avg = int(round(avg, 0))
    liczaj = abs(avg - int(peoples_age[0]))
    for i in range(table_len):
        if abs(avg - int(peoples_age[i])) < liczaj:
            closest_number = abs(avg - int(peoples_age[i]))

    for i in range (table_len):
        if int(peoples_age[i]) == avg + closest_number or int(peoples_age[i]) == avg - closest_number:
            closest_to_avarage.append(table[i])

    return closest_to_avarage

