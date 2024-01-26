import random
import string

def generate_password(min_length = 12, include_special_chars= True, include_numbers = True):
    alphabets = string.ascii_letters # both uppercase and lowercase letters
    numbers = string.digits # digits from 0-9
    special_chars = string.punctuation # includes !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    all_characters = alphabets
    password = ""

    if include_special_chars:
        all_characters = f"{all_characters}{special_chars}"
    if include_numbers:
        all_characters = f"{all_characters}{numbers}"


    while len(password) < min_length:
        char = random.choice(all_characters) # selects a random character
        password = f"{password}{char}"
    
    return password

print(generate_password())
    
