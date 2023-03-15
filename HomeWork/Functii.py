# 1. Scrieti o functie care verifica daca unu nr este par.
# Daca este par returneaza True, altfel False. Functia are un singur argument.

# def odd_even(number):
#     """Returns True for even, False for odd"""
#     if number % 2 == 0:
#         return True 
#     else:
#         return False



# 2. Utilizati functia de la pct 1 pentru a afisa toate numerele impare in intervalul
# [0, 50] si in intervalul [2000, 2100].

# for i in range(51):
#     if not odd_even(i):
#         print(i)

# list1 = range(51)
# list2 = range(2000, 2101)


# def odd_even(number):
#     """Prints odd numbers"""
#     odd_list = []
#     for i in number:
#         if i % 2 != 0:
#             odd_list.append(i)
#     print(odd_list)

# odd_even(list2)

# def odd_even_1():
#     for i in list1:
#         if i % 2 != 0:
#             odd_list_1.append(i)
#     print(odd_list_1)
        
# def odd_even_2():
#     for i in list2:
#         if i % 2 != 0:
#             odd_list_2.append(i)
#     print(odd_list_2)

# odd_even_1()


# 5. Scrieti o functie care returneaza volumul unui cilintru in litri,
# Aceasta va primi doua argumente reprezentand inaltimea si raza bazei in metri.

#  v = pi*r^2h

# PI = 3.14

# def volum_cilindru(r, h):
#     v = PI * r ** 2 * h 
#     print(v)

# volum_cilindru(5, 10)

"""9. Managerul de la fabrica de cutii are nevoie de un program care calculeaza pretul
cutiilor in functie de dimensiunea si grosimea lor. Pentru o cutie cu volumul de 1000 de litri
de gorsime 1, pretul este de 25 de lei.
Pentru gorosimile 2 si 3, pretul creste cu 10 respectiv 20 la suta.
Scrieti o functie care primeste 4 parametrii:
- inaltimea cutiei
- latimea cutiei
- lungimea cutiei
- tipul de carton (1, 2 sau 3)
Functia returneaza pretul."""

# V= 1m x 1m x 1m = 1 m3

def get_price(height, latitude, length, type):
    price_brut = height * latitude * length * 25
    if type == 2:
        return price_brut * 1.1 
    if type == 3:
        return price_brut * 1.2 
    return price_brut

print(f"Pret cutie: {get_price(1, 1, 1, 4)} ")

