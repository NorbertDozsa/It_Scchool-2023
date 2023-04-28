MENU = {
    1: "Add Contact",
    2: "Search Contact",
    3: "Delete Contact"
}

contacts_n = []
contacts_p = []
czip = zip(contacts_n,contacts_p)

contacts = dict(czip)

def add_contact():
    """Adds contact to Agenda"""
    name = input("Name: ")
    number = input("Number: ")
    contacts_n.append(name)
    contacts_p.append(number)
    

def search_contact():
    """Searches contact in Agenda"""

    search = input(f"Search contact: ")
    try:
        for i in contacts:
            if search in i:
                    print(i)
            else:
                    raise ValueError(f"Can't find this contact: {search}")
            break
    except ValueError:
        print(f"Can't find this contact: {search}")

def delete_contact():
    """Deletes contact from Agenda"""

    delete_c = input(f"Delete contact: ")
    try:
        if delete_c in contacts:
                contacts.pop(delete_c)
        else:
            raise ValueError(f"Can't find this contact to delete: {delete_c}")
    except ValueError:
            print (f"Can't find this contact to delete: {delete_c}")



def get_answer():
    while True:
        try:
            print(MENU)
            answer = input(f"Select an action from above ")
            if answer == "1":
                add_contact()
            elif answer == "2":
                search_contact()
            elif answer == "3":
                delete_contact()
            else:
                 raise ValueError(f"Your answer '{answer}' doesn't match the menu options!")
        except ValueError:
                print(f"Your answer '{answer}' doesn't match the menu options!")


# get_answer()
add_contact()
print(contacts_n)
print(contacts_p)
print(czip)
print(contacts)


