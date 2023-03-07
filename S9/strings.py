# import_numbers = "today we had 280 clients."

# new_numb = import_numbers.replace("280 clients.", "300 customers !")

# print(new_numb.title())

# for w in new_numb:
#     print(w)

# lorem = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."   

# words = lorem.split(" ")

# for w in lorem:
#     print(w)
    

# print(len(words))


py_text = """Python is an interpreted, interactive, object-oriented programming language. It incorporates modules, exceptions, dynamic typing, very high level dynamic data types, and classes. It supports multiple programming paradigms beyond object-oriented programming, such as procedural and functional programming. Python combines remarkable power with very clear syntax. It has interfaces to many system calls and libraries, as well as to various window systems, and is extensible in C or C++. It is also usable as an extension language for applications that need a programmable interface. Finally, Python is portable: it runs on many Unix variants including Linux and macOS, and on Windows.
To find out more, start with The Python Tutorial. The Beginner's Guide to Python links to other introductory tutorials and resources for learning Python."""
# py_test_lower = py_text.lower()
word_in_text = py_text.split(" ")
stats_with_a = []

# for a in word_in_text:
#     if a.startswith("a"):
#         stats_with_a.append(a)
#     print(count(stats_with_a))

    
    

for s in word_in_text:
    if s.startswith("a"):
        print(s)
