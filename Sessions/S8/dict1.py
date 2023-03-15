# dict1 = {
#     "key1": 1,
#     "key2": {
#         "key1": 1,
#         "key2": ["elem1", "elem2"]
#    }
# }
# # print(dict1)

# # lista_dict = dict1["key2"]

# # print(lista_dict)\

# print(dict1["key2"]["key2"][1])

# dict2 = {
#     "Alex": 21,
#     "Maria": 23,
#     "Ion": 25
# }

# for v, k in dict2.items():
#     print(v, k)

# dict3 = {
#     "Alex": [7, 5, 7],
#     "Maria": [8, 9, 5],
#     "Ion": [6, 7, 8]
# }

# for k, v  in dict3.items():
#     print(k, sum(v) / len(v))

students_grades = {
    'Ana': 9.5,
    'Ioan': 8.0,
    'Maria': 7.5,
    'Andrei': 9.0,
    'Elena': 10.0
}

# for k in students_grades.keys():
#     print(k)

sort_inv = sorted(students_grades.keys(), reverse=True)

print(sort_inv)

for k in sorted(students_grades.keys(), reverse=True):
    print(k)


    