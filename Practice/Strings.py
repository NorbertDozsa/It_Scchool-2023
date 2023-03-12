lorem = """Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""

product_code_list = [
    "mmf2",
    "xdfr",
    "ef3r",
    "efc2",
    "sddf"
    "weee"
]

import_numbers = "Today we had 280 clients."

commit = """commit 30c06bce50eeb7a8856e18df2dc64e76fec14cc9
Author: Dinu Mihai <mihai.dinu93@gmail.com>
Date:   Thu Jun 9 18:18:02 2022 +0300

    shuffle method"""

py_text = """Python is an interpreted, interactive, object-oriented programming language. It incorporates modules, exceptions, dynamic typing, very high level dynamic data types, and classes. It supports multiple programming paradigms beyond object-oriented programming, such as procedural and functional programming. Python combines remarkable power with very clear syntax. It has interfaces to many system calls and libraries, as well as to various window systems, and is extensible in C or C++. It is also usable as an extension language for applications that need a programmable interface. Finally, Python is portable: it runs on many Unix variants including Linux and macOS, and on Windows.
To find out more, start with The Python Tutorial. The Beginner's Guide to Python links to other introductory tutorials and resources for learning Python."""

# 1)

words = lorem.split(" ")
# print()
# print("*" * 50)
last_10_words = (f"Ultimele 10 cuvinte sunt: {words[:78:-1]}")
first_10_words = (f"Primele 10 cuvinte sunt: {words[:10:]}")
print(last_10_words)
print()
print(first_10_words)

# 2)

for i, v in product_code_list:
    product_code_list[i] = v[:-1] + "x"

print(product_code_list)

# 3)

words_list = [

]

for w in words:
    words_list.append(words)
    break

print(type(words_list))
print(words_list)

# 4)

one_string = " ".join(product_code_list)

print(one_string)

# 5)

# prev = 0

words_import_numbers = import_numbers.split(" ")

print(words_import_numbers[3])

# 6)

prop = " ".join(product_code_list)

print(f"First letter capitalized: {prop.capitalize()}")
print(f"Every first letter capitalized: {prop.title()}")

# 7)

first_20_lorem = words[:20]

comma = first_20_lorem.find(",")

lines = lorem.split("\n")

print(comma)
