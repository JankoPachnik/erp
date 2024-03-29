""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
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

    # your code
    module_active = 1
    while module_active == 1:
        options_inventory = ["Show table",
                             "Add",
                             "Remove",
                             "Update",
                             "get longest name id",
                             "get subscribed emails"]
        file_directory = 'crm/customers.csv'
        table = data_manager.get_table_from_file(file_directory)
        ui.print_menu("CRM menu", options_inventory, "Exit program")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
            data_manager.write_table_to_file(file_directory, table)
        elif option == "3":
            id_ = ui.get_inputs(['id: '], "Please provide ID of a record you want to delete")
            remove(table, id_[0])
            data_manager.write_table_to_file(file_directory, table)
        elif option == "4":
            id_ = ui.get_inputs(['id: '], "Please provide ID of a record you want to edit")
            update(table, id_[0])
            data_manager.write_table_to_file(file_directory, table)
        elif option == "5":
            get_longest_name_id(table)
        elif option == "6":
            get_subscribed_emails(table)
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
    title_list = ["id", "name", "email", "subscribed"]
    ui.print_table(table, title_list)

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
        game_data = ui.get_inputs(['Name: ', 'email: ', 'subscribed: '],
                                  "Please provide information about customer")
        new_row = (unique_id, game_data[0], game_data[1], game_data[2])
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
                game_data = ui.get_inputs(['Name ({}): '.format(table[i][1]), 'E-mail ({}): '.format(table[i][2]),
                                           'Subscribed ({}): '.format(table[i][3])],
                                          "Please update information about product")
                if game_data[0] != '':
                    table[i][1] = game_data[0]
                if game_data[1] != '':
                    table[i][2] = game_data[1]
                if game_data[2] != '':
                    table[i][3] = game_data[2]
    except ValueError:
        ui.print_error_message('The ID you are trying to reach is currently unavailable')
    return table


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """

    # your code6

    all_items = []
    longest_now = 0
    result = 0

    names_ID = [table[1] for table in table]
    full_name = [table[0] for table in table]

    for element in range(len(names_ID)):
        all_items = names_ID
        all_items[element] += full_name[element]

    result = []
    for i in all_items:
        new = len(i)
        if new >= longest_now:
            longest_now = new
            result.append(i)

    result = max(result)
    result = result[-8:]
    label = "longest name"
    ui.print_result(result, label)
    return result



# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """

    # your code

    email = [table[1] for table in table]
    names = [table[2] for table in table]
    subsc = [table[3] for table in table]
    lista = []
    for element in range(len(names)):
        lista = names
        lista[element] += ";"
        lista[element] += email[element]
        lista[element] += ";"
        lista[element] += subsc[element]

    element = 0
    while element < len(lista):
        if lista[element][-1] == "0":
            lista.pop(element)
        else:
            element += 1

    for element in range(len(lista)):
        lista[element] = lista[element][:-2]

    label = "get_subscribed_emails"
    result = lista
    ui.print_result(result, label)
    return result
