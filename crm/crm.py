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
        customer = input('Please write a name of a customer\n')
        email = input('Please write an email\n')
        status = input('Please write if a customer is Active\n')
        new_row = (unique_id, customer, email, status)
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
                customer = input('Update name of a Customer (current: {})\n'.format(table[i][1]))
                email = input('Update email (current: {})\n'.format(table[i][2]))
                status = input('Update status (current: {})\n'.format(table[i][3]))
                if customer != '':
                    table[i][1] = customer
                if email != '':
                    table[i][2] = email
                if status != '':
                    table[i][3] = status
    except ValueError:
        print('The ID you are trying to reach is currently unavailable')
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

    # your code


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
