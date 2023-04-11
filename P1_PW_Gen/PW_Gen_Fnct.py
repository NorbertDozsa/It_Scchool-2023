import random

numbers = []
symbols = []
abc = []


# for n in range(48, 58):
#     numbers.append(chr(n))

# for a in range(65, 91):
#     abc.append(chr(a))

# for b in range(97, 123):
#     abc.append(chr(b))

# for x in range(33, 48):
#     symbols.append(chr(x))


# intr-o functie, list comprehension

def get_pw_length():
    """Retrieves Password's Length."""

    while True:
        try:
            password_length = int(input(f"Please set your password length: "))
            break
        except ValueError:
            print("Please answer with a number!")
    return password_length

def get_user_use_digit():
    """Retrieves if the user wants to use digits in his password or not."""
    
    while True:
        try:
            use_digits = input(f"Do you want to use digits in your password? (yes/no): ")
            if use_digits == "yes":
                return True
            if use_digits == "no":
                return False
            else:
                raise ValueError("Incorrect answer!")
        except ValueError:
                print("Please answer with yes or no!")
              
def get_user_use_symbols():
    """Retrieves if the user wants to use symbols in his password or not."""
  
    while True:
        try:
            use_symbols = input(f"Do you want to use symbols in your password? (yes/no): ")
            if use_symbols == "yes":
                return True
            if use_symbols == "no":
                return False
            else:
                raise ValueError("Incorrect answer!")
        except ValueError:
                print("Please answer with yes or no!")


def get_password():
    """Generates Passwords for Users."""
    user_length = get_pw_length()
    user_digits = get_user_use_digit()
    user_symbols = get_user_use_symbols()
    password = []
    while len(password) < user_length:
        # password.append(random.choice(abc)) + un if     
        if user_digits == True:
            password.append(random.choice(numbers))
        if user_symbols == True:
            password.append(random.choice(symbols))
    
    print(f"Your password is: {''.join(password)}")


get_password()


# def get_password():
#     """Generates Passwords for Users."""
#     pw_length = get_pw_length()50
#     password = []
#     while len(password) < pw_length:
#         password.append(list(set(abc_lower))[0+1])
#         password.append(list(set(abc_upper))[0+1])       
#     if get_user_use_digit() == True:
#             password.append(list(set(numbers))[0+1])
#     if get_user_use_symbols() == True:
#             password.append(list(set(symbols))[0])
    
#     return "".join(password)