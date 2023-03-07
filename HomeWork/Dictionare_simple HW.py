# nume_varsta = {
#      "Norbert": 25,
#      "Andreea": 28,
#     "Mihaela": 28
# }

# # print(type(nume_varsta))

# for n, v in nume_varsta.items():
#     print(n, v)


# #     ex 3. Creați un dicționar cu numele și salariul a trei angajați.
# # Afișați salariatul cu cel mai mare salariu.

# salarii_angajati = {
#     "Andrei" : 3800,
#     "Andreea" : 5500,
#     "Mircea" : 8000,
#     }

# salariul_celmare = 0
# numele = ""

# for n, s in salarii_angajati.items():
#     if s >= salariul_celmare:
#         salariul_celmare = s
#         numele = n
# print(numele)
    
# #     4. Creați un dicționar cu numele și data de naștere a trei persoane.
# # Adăugați o nouă persoană la dicționar și afișați numele și data de naștere a
# # tuturor persoanelor.  

# nume_datanasterii = {
#     "Andreea" : "13, Feb",
#     "Norbert" : "12, Iun",
#     "Mirce" : "25, Dec" , 
# }

# nume_datanasterii["Ioan"] = "3, Martie"

# for name, data in nume_datanasterii.items():
#     print(name, data)

# #     5. Creați un dicționar cu numele și adresa a trei prieteni.
# # Modificați adresa celui de-al doilea prieten și afișați dicționarul actualizat.

# name_adress = {
#     "Andreea" : "Constanta",
#     "Norbert" : "Cluj",  
#     "Romeo" : "Cluj"
#     }

# name_adress["Norbert"] = "Constanta"

# for n, a in name_adress.items():
#     print(n, a)


# # 6. Creați un dicționar cu numele și vârsta a trei persoane.
# # Ștergeți persoana cu vârsta cea mai mică și afișați dicționarul actualizat.

# nume_varsta = {
#     "Norbert": 25,
#     "Andreea": 28,
#     "Mihaela": 28
# }


# cel_tanar = 99
# cel_tanar_name = ""

# for n, v in nume_varsta.items():
#     if v < cel_tanar:
#         cel_tanar = v
#         cel_tanar_name = n
# del nume_varsta[cel_tanar_name]

# print(nume_varsta)

# #    8. Creați un dicționar cu numele și numărul de telefon a trei prieteni.
# # Afișați numerele de telefon în ordine alfabetică a numelor.

# contacts = {
#     'Alice': '0721123456',
#     'John': '0743123456',
#     'Bob': '0732123456'
# }

# for name, number in sorted(contacts.items()):
#     print(name, number)

