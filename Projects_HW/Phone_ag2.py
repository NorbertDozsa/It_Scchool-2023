while True:
    q = input("Add Contact (1) Search Contact (2) Delete Contact (3): ")
    if q == "1":
        with open('contact.txt', 'a') as f:
            name = input("Name: ")
            phone = input("Number: ")
            f.writelines((name,' : ', phone, '\n'))
    if q == "2":
        with open('contact.txt', 'r') as f:
            search = input("Search Contact: ")
            for i in f:
                if search in i:
                    print(i)
    if q == "3":
        with open('contact.txt', '') as f:
            name = input("Name: ")
            phone = input("Number: ")
            f.__del__()


