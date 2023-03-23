# 1. Scrieti un program care sa imparta doua numere intregi citite de la tastatura si sa afiseze catul si restul.
# In cazul in care impartirea nu poate fi realizata (de exemplu, in cazul in care al doilea numar este 0), programul ar trebui sa afiseze un mesaj corespunzator de eroare.


# a = int(input("Primul numar este:"))
# b = int(input("Al doilea numar este:"))
# try:
#     cat = a // b
#     rest = a % b 
#     print(f"Catul impartirii este {cat}")
#     print(f"Restul impartirii este {rest}")
# except ZeroDivisionError:
#     print(f"Nu sa putut imparti la {b}")

# 2. Scrieti un program care sa ceara utilizatorului sa introduca un numar intreg, iar apoi sa afiseze acel numar ridicat la puterea a doua. 
# Daca utilizatorul introduce un input invalid (de exemplu, un numar cu virgula), programul ar trebui sa afiseze un mesaj corespunzator de eroare.



x = int(input("Introduceti un numar: "))
try:
    x**2
except ValueError:
    print(f"Introduceti doar numere intregi!") 

        

   


