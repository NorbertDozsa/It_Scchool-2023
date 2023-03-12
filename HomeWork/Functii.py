# 1. Scrieti o functie care verifica daca unu nr este par.
# Daca este par returneaza True, altfel False. Functia are un singur argument.

def odd_even(number):
    """Returns True for even, False for odd"""
    if number % 2 == 0:
        print(True) 
    else:
        print(False)


# 2. Utilizati functia de la pct 1 pentru a afisa toate numerele impare in intervalul
# [0, 50] si in intervalul [2000, 2100].

list1 = range(50)
list2 = range(2000, 2100)


def odd_even(number):
    """Prints odd numbers"""
    odd_list = []
    for i in number:
        if i % 2 != 0:
            odd_list.append(i)
    print(odd_list)

odd_even(list2)

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
