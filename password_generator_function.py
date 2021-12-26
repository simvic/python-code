#Password Generator Project
import random
def password_generator(nr_letters, nr_numbers, nr_symbols):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = []
    for val in range(1, nr_letters + 1):
        picked_letters = random.choice(letters)  
        password.append(picked_letters) 


    for symbol in range(nr_symbols + 1):
        picked_symbols = random.choice(symbols) 
        password.append(picked_symbols)


    for numbers in range(nr_numbers + 1):
        picked_numbers = random.randint(0, numbers)
        password.append(str(picked_numbers))

    random.shuffle(password)
    hard_password = ' '.join([str(item) for item in password])

    return hard_password

