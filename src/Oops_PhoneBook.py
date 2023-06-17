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

    databook = {}

    def __init__(self, name, number, email) -> None:
        self.name = name
        self.number = number
        self.email = email
        self.update = str(datetime.datetime.now())

    def load_phonebook():
        """Loads existing databook

        Returns:
            databook(dict): Currently loaded dictionary
        """
        Contact.databook = pd.read_csv("../assets/phonebook.csv")
    
    def display() -> None:
        """Returns current databook into a dataframe

        Returns:
            df(DataFrame): Current databook
        """
        Contact.load_phonebook()
        current_phonebook = pd.DataFrame(Contact.databook)
        print("\n>>> Current Phonebook | Number of entries : {} <<<".format(current_phonebook.shape[0]))
        print("========================================================================")
        print(current_phonebook,)
        print("========================================================================\n\n")

    def add() -> None:
        """Adds contact to databook"""
        Contact.load_phonebook()
        name = input("Enter contact name : ")
        number = input("Enter contact number : ")
        email = input("Enter contact email : ")
        contact = Contact(name, number, email)
        
        Contact.databook["NAME"].append(contact.name)
        Contact.databook["NUMBER"].append(contact.number)
        Contact.databook["EMAIL"].append(contact.email)
        Contact.databook["UPDATE"].append(str(datetime.datetime.now()))
        print("\nContact added succesfully !\n")

        pd.DataFrame(Contact.databook).to_csv("../assets/phonebook.csv")

    def prompt() -> None:
        """Prompts user for input

        Returns:
            letter(str): p, a, d, s, u
        """
        print("Available Functionality: ")
        print("========================================================================")
        print("p: Print Contacts | a: Add | d: Delete | s: Search | u: Update | q: Quit")
        print("========================================================================")
        return input("Enter function: ")


# %%
def main():
    """Main function for Phonebook"""
    print("\n\n>>> Phone Book <<<")
    Contact.load_phonebook()
    print(f"No of contacts : {Contact.databook.shape[0]}")

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
