

MENU = {
    1 : "Add Contact",
    2 : "Search Contact",
    3 : "Delete Contact"
}

# contacts = []

class PhoneAgenda:
    """Represents a phone agenda"""
    
    def __init__(self):
        self.__contact = []

    @property
    def contact(self):
        return self.__contact
    

    def add_contact():
        name = input(f"Name: ")
        number = input(f"Number: ")
        self.__contact.append name
        


    def search_contact():
        while True:
            try:
                search = input("Search Contact:")
                for i in self.__contacts:
                    if search in i:
                        print(i)
            except ValueError:
                print(f"Can't find this contact: {search}")


    def delete_contact():
        pass


