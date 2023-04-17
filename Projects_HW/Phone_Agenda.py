meniu = {
    1: "Add Contact",
    2: "Search Contact",
    3: "Delete Contact"
}

def get_answer():
    print(meniu)
    while True:
        try:
            answer = int(input(f"What do you choose to do?: "))
            if answer in range(1,4):
                return answer
            else:
                raise ValueError("Please choose an action form the Menu !")
        except ValueError:
            print("Please choose an action form the Menu !")

def add_contact():
    if get_answer() == 1:
        