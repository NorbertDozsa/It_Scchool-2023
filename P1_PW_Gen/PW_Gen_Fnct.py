import random

numbers = []
abc_lower = []
abc_upper = []
symbols = []


for n in range(48, 58):
    numbers.append(chr(n))
for a in range(65, 91):
    abc_upper.append(chr(a))
for b in range(97, 123):
    abc_lower.append(chr(b))
for x in range(33, 48):
    symbols.append(chr(x))


def get_pw_length(*password_length: int):
    """Retrieves Password's Length."""

    while True:
        try:
            password_length = int(input(f"Please set your password length: "))
            break
        except ValueError:
            print("Please answer with a number!")
    return password_length

def get_user_use_digit(*use_digits: bool):
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
              
def get_user_use_symbols(*use_symbols: bool):
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
    pw_length = get_pw_length()
    use_digits = get_user_use_digit()
    use_symbols = get_user_use_symbols()
    password = []
    while len(password) < pw_length:
        password.append(random.choice(abc_lower))
        password.append(random.choice(abc_upper))       
        if use_digits == True:
            password.append(random.choice(numbers))
        if use_symbols == True:
            password.append(random.choice(symbols))
    
    pw = "".join(password)
    print(f"Your password is: {pw}")


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