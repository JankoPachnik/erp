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
    options_inventory = ["Show table",
                         "Add",
                         "Remove",
                         "Update",
                         "get longest name id",
                         "get subscribed emails"]
    file_directory = 'crm/customers.csv'
    ui.print_menu("CRM Menu", options_inventory, "Exit program")
    table = data_manager.get_table_from_file(file_directory)
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(table)
    elif option == "2":
        add(table)
    elif option == "3":
        remove(table, id_)
    elif option == "4":
        update(table, id_)
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

    # your code


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code

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

    # your code

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

    # your code

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
    all_items = [table[1] for table in table]
    longest_now = 0
    result = 0
    for i in all_items:
        result = 0
        new = len(i)
        if new >= longest_now:
            longest_now = new
            result = i
    label = "longest name"
    ui.print_result(result, label)


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
    for i in range(len(names)):
        lista = names
        lista[i] += ":"
        lista[i] += email[i]
        lista[i] += ":"
        lista[i] += subsc[i]
    for i in range(len(lista)):
        if lista[i][-1] == 0:
            lista.remove(lista)

    for i in range(len(lista)):
        print(lista[i])
