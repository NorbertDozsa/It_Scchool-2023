# Matrice

matrix = [
    ["Ionel", [8, 6, 5, 9, 8]],
    ["Gigel", [5, 7, 8, 6, 8]],
    ["Ana", [8, 9, 8, 9, 10]],
    ["Ioana", [7, 8, 8, 7, 6]],
    ["Matei", [4, 5, 5, 4, 3]],
]


# medie_ionel = sum(matrix[0][1]) / len(matrix[0][1])
# medie_gigel = sum(matrix[1][1]) / len(matrix[1][1])
# medie_ana = sum(matrix[2][1]) / len(matrix[2][1])
# medie_ioana = sum(matrix[3][1]) / len(matrix[3][1])
# medie_matei = sum(matrix[4][1]) / len(matrix[4][1])

medii = [sum(x) / len(x) for x in zip(matrix[0][1])]

print(medii)




# print(len(medie))
# for i in range(2,)    
# medie.sort

# for i in matrix:
#     print(i[0], "medie", sum(i[1])/len(i[1]))


# Exercitiul 1

# input_list = []

# n = int(input("nr elemente: "))

# for i in range(n):
#      input_list.append(int(input()))

# # input_list_sorted = sorted(input_list)

# if input_list == sorted(input_list):
#      print("True")
# else:
#      print("False")

# print(input_list)



# Exercitiul 2

# a = [2, 3, 44, 55, 6]
# b = [55, 6, 77, 3, -2]

# c = []
# for i1, i2 in zip(a, b):
#     c.append(i1 * i2) 

# # c.append(a[0] * b[0])
# # c.append(a[1] * b[1])
# # c.append(a[2] * b[2])
# # c.append(a[3] * b[3])
# # c.append(a[4] * b[4])

# # print(tuple(zip(a, b)))

# print(c)