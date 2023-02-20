# Ex 1 . Scrie un program care citeste de la tastatura un numar 
# natural si afiseaza "Par" daca numarul este par sau "Impar" 
# daca numarul este impar.

# number = int(input("Number:"))
# odd = number % 2
# if odd != 1:
#     print("Even")
# else:
#     print("Odd")

# Ex 2 . Scrie un program care citeste de la tastatura un numar 
# natural, reprezentand raza unui cerc, si afiseaza perimetrul
# cercului insotit de mesajul "Perimetru cercului = <valoare>".
# Daca numarul citit este mai mare decat 100 se va calcula si aria
# cercului. Aceasta se va afisa insotita de mesajul "Aria cercului = <valoare>".

# r = int(input("Raza="))
# PI = 3.14
# perimetrul_cercului = 2 * pi * r 

# print(perimetrul_cercului)

#  Ex 3 .  Scrie un program care citeste de la tastatura doua numere, a si b.
# Daca a > b sa se diferenta suma lor.
# Daca a == b sa se afiseze a la puterea b
# Altfel sa se afiseze suma lor.

# a = int(input("a = "))
# b = int(input("b = "))

# if a > b:
#     print(a - b)
# elif a == b:
#     print(a ** b)
# else:
#     print(a + b)

#  Ex 4 .  Scrie un program care citeste de la tastatura doua numere,
# si calculeaza a / b daca a > b sau b / a daca a <= b. Afiseaza 
# rezultatul.

# a = int(input("a = "))
# b = int(input("b = "))
# a_div_b = a / b
# b_div_a = b / a

# if a > b:
#     print("Rezultat:", a_div_b)
# elif a <= b:
#     print("Rezultat:", b_div_a)

#  Ex 5 . Scrie un program care citeste de la tastatura un numar 
# natural pozitiv din 3 cifre. Daca numarul introdus nu are 3 cifre sau 
# este un numar negativ se afiseaza: "Eroare".
# Daca ultima cifra din numarul introdus este mai mare sau egala cu 5,
# se va afisa suma dintre numarul introdus si ultima sa cifra, altfel 
# se va afisa diferenta dintre numarul introdus si ultima sa cifra.


# numar = int(input("Numar: "))
# last_digit = int(repr(numar)[-1])

# # print(last_digit)

# if numar < 99:
#     print("Eroare")
# elif numar > 999:
#     print ("Eroare")
# elif numar < 0:
#     print("Eroare")
# elif last_digit >= 5:
#     print(numar + last_digit)
# else:
#     print(numar - last_digit)