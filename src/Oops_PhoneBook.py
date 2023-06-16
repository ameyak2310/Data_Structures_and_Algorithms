""" 
Phonebook
"""
# %%
import datetime
import pandas as pd


class Contact:
    """Class Contact to store contents of Phonebook

    Returns:
        None: Performs functions as defined in main app
    """

    databook = {
        "NAME": [],  # ["Default"],
        "NUMBER": [],  # [00000],
        "EMAIL": [],  # ["default@default.com"],
        "UPDATE": [],  # ["2023-06-16 17:13:28.161998"],
    }

    def __init__(self, name, number, email) -> None:
        self.name = name
        self.number = number
        self.email = email
        self.update = str(datetime.datetime.now())

    def add() -> None:
        """Adds contact to databook"""
        name = input("Enter contact name : ")
        number = input("Enter contact number : ")
        email = input("Enter contact email : ")
        contact = Contact(name, number, email)
        Contact.databook["NAME"].append(contact.name)
        Contact.databook["NUMBER"].append(contact.number)
        Contact.databook["EMAIL"].append(contact.email)
        Contact.databook["UPDATE"].append(str(datetime.datetime.now()))
        print("\nContact added succesfully !")

    def display() -> None:
        """Returns current databook into a dataframe

        Returns:
            df(DataFrame): Current databook
        """
        current_phonebook = pd.DataFrame(
            data=Contact.databook, columns=["NAME", "NUMBER", "EMAIL", "UPDATE"]
        )
        print("\n Current Phonebook")
        print("\n\n--------------------")
        print(current_phonebook, "\n")
        print("--------------------\n\n")
        return current_phonebook

    def prompt() -> None:
        """Prompts user for input

        Returns:
            letter(str): p, a, d, s, u
        """
        print(
            "\nAvailable Functionality : \n",
            "p: Print Contacts | a: Add | d: Delete | s: Search | u: Update | q: Quit",
        )
        return input("Enter function: ")


# %%
def main():
    """Main function for Phonebook"""
    print("\n\n>>> Phone Book <<<")
    print(f"No of contacts : {Contact.display().shape[0]}")

    status = True
    while status:
        function = Contact.prompt()

        if function == "p":
            Contact.display()

        elif function == "a":
            Contact.add()

        elif function == "q":
            status = False


# %% Main App Call
if __name__ == "__main__":
    main()
