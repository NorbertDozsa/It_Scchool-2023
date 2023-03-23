# 3) Make a script which encrypts a string using Caesar cipher with key 20, use a function to generate a dict representing the new alphabet
#     A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z
#     Y	Z   A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X

#  caesar {
#         "A": "Y",
#         "B": "Z",
#         "C": "A"
#     }

#     def get_alphabet(key):
#         generate new alphabet
#         return dict with alphabet

#     def crypt(msj, key):
#         alphabet = get_alphabet(key)
#         return msaj cripta

#     crypt("Mesajul", 20)


# import string

# def get_alfabet(start, value):
#     return {chr(ord('a') + i) : 0 for i in range(value)}

# print(get_alfabet('a', 26))

def gen_abc():
    return{(chr(i), chr(i)) for i in range(97, 123)}

print(gen_abc())


# def get_alphabet():
#     alphabet = dict.fromkeys(string.ascii_lowercase, "")
    
    
    
#     return alphabet

# print(get_alphabet())
  
