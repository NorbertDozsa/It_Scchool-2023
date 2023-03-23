# 1. Sa se scrie o functie care primeste o lista de numere si verifica daca toate numerele sunt pozitive.
# Functia trebuie sa returneze True daca toate numerele sunt pozitive, si False altfel. Folositi functia all.

def verify_if_positive(lst):
    """Verifies if the given list numbers are greater than 0."""
    return all(i > 0 for i in lst)
      
init_lst = [4, 56, -1, 5, 45]
init_lst2 = [5, 50, 1, 4, 45]

print(verify_if_positive(init_lst))

# print(all(init_lst))

# 2. Sa se scrie o functie care primeste o lista de numere si verifica daca exista cel putin un numar pozitiv.
# Functia trebuie sa returneze True daca exista cel putin un numar pozitiv, si False altfel. Folositi functia any.

def verify_positive_nr(lst):
    """Verifies if the given list has at least one number greater than 0."""
    return any(i > 0 for i in lst)

print(verify_positive_nr(init_lst))

# 3. Sa se scrie o functie care primeste o lista de cuvinte si returneaza un dictionar care contine cuvintele ca si chei, si pozitia lor in lista ca si valori. 
# Folositi functia enumerate.

words = ['Python', 'is', 'an', 'easy', 'to', 'learn', 'powerful', 'programming', 'language', 'It', 'has', 'efficient', 'high-level', 'data', 'structures', 'and', 'a', 'simple', 'but', 'effective', 'approach', 'to', 'object-oriented', 'programming', 'Python’s', 'elegant', 'syntax', 'and', 'dynamic', 'typing', 'together', 'with', 'its', 'interpreted', 'nature', 'make', 'it', 'an', 'ideal', 'language', 'for', 'scripting', 'and', 'rapid', 'application', 'development', 'in', 'many', 'areas', 'on', 'most', 'platforms', 'The', 'Python', 'interpreter', 'and', 'the', 'extensive', 'standard', 'library', 'are', 'freely', 'available', 'in', 'source', 'or', 'binary', 'form', 'for', 'all', 'major', 'platforms', 'from', 'the', 'Python', 'web', 'site', 'https://www.python.org', 'and', 'may', 'be', 'freely', 'distributed', 'The', 'same', 'site', 'also', 'contains', 'distributions', 'of', 'and', 'pointers', 'to', 'many', 'free', 'third', 'party', 'Python', 'modules', 'programs', 'and', 'tools', 'and', 'additional', 'documentation', 'The', 'Python', 'interpreter', 'is', 'easily', 'extended', 'with', 'new', 'functions', 'and', 'data', 'types', 'implemented', 'in', 'C', 'or', 'C++', '(or', 'other', 'languages', 'callable', 'from', 'C)', 'Python', 'is', 'also', 'suitable', 'as', 'an', 'extension', 'language', 'for', 'customizable', 'applications', 'This', 'tutorial', 'introduces', 'the', 'reader', 'informally', 'to', 'the', 'basic', 'concepts', 'and', 'features', 'of', 'the', 'Python', 'language', 'and', 'system', 'It', 'helps', 'to', 'have', 'a', 'Python', 'interpreter', 'handy', 'for', 'hands-on', 'experience', 'but', 'all', 'examples', 'are', 'self-contained', 'so', 'the', 'tutorial', 'can', 'be', 'read', 'off-line', 'as', 'well', 'For', 'a', 'description', 'of', 'standard', 'objects', 'and', 'modules', 'see', 'The', 'Python', 'Standard', 'Library', 'The', 'Python', 'Language', 'Reference', 'gives', 'a', 'more', 'formal', 'definition', 'of', 'the', 'language', 'To', 'write', 'extensions', 'in', 'C', 'or', 'C++', 'read', 'Extending', 'and', 'Embedding', 'the', 'Python', 'Interpreter', 'and', 'Python/C', 'API', 'Reference', 'Manual', 'There', 'are', 'also', 'several', 'books', 'covering', 'Python', 'in', 'depth', 'This', 'tutorial', 'does', 'not', 'attempt', 'to', 'be', 'comprehensive', 'and', 'cover', 'every', 'single', 'feature', 'or', 'even', 'every', 'commonly', 'used', 'feature', 'Instead', 'it', 'introduces', 'many', 'of', 'Python’s', 'most', 'noteworthy', 'features', 'and', 'will', 'give', 'you', 'a', 'good', 'idea', 'of', 'the', 'language’s', 'flavor', 'and', 'style', 'After', 'reading', 'it', 'you', 'will', 'be', 'able', 'to', 'read', 'and', 'write', 'Python', 'modules', 'and', 'programs', 'and', 'you', 'will', 'be', 'ready', 'to', 'learn', 'more', 'about', 'the', 'various', 'Python', 'library', 'modules', 'described', 'in', 'The', 'Python', 'Standard', 'Library']


def word_dict(lst):
    """Creates a dict from the given list, with the words as keys and positions as values."""
    for i in enumerate(lst):
       print(f"Words: {i[1]}, ... Position: {i[0]}")
    

word_dict(words)


# 4. Sa se scrie o functie care primeste doua liste de numere si returneaza o lista care contine suma elementelor de pe aceleasi pozitii. Folositi functia zip.

from faker import Faker
from faker import Faker
fake = Faker("ro_RO")

phone_nr = []
names = []

for i in range(10):
    names.append(fake.name())

# print(names)

Faker.seed(0)
for i in range(10):
    phone_nr.append(fake.phone_number())

# print(phone_nr)

def gen_zip(name, phone_number):
    """Creates a dict with names and their phone number."""
    return dict(zip(name, phone_number))

print(gen_zip(names, phone_nr))


def gen_sum_list(lst1, lst2):
    """Creates a list with the sum of 2 lists"""
    new_list = [sum(i) for i in zip(lst1,lst2)]
    return new_list

        
    

print(gen_sum_list(init_lst, init_lst2))

