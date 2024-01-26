import random
import string

def generate_password(include_special_chars, include_numbers, min_length=12):
    include_special_chars = include_special_chars == "on"
    include_numbers = include_numbers == "on"
    alphabets = string.ascii_letters # both uppercase and lowercase letters
    numbers = string.digits # digits from 0-9
    special_chars = string.punctuation # includes !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    all_characters = alphabets
    password = ""

    if include_special_chars:
        all_characters = f"{all_characters}{special_chars}"
    if include_numbers:
        all_characters = f"{all_characters}{numbers}"

    criteria = False
    contain_numbers = False
    contain_special_chars = False


    while not criteria or len(password) < int(min_length):
        char = random.choice(all_characters) # selects a random character
        password = f"{password}{char}"
        if char in numbers:
            contain_numbers =  True
        elif char in special_chars:
            contain_special_chars = True



        criteria = True
        if include_numbers:
            criteria = contain_numbers
        if include_special_chars:
            criteria = criteria and contain_special_chars



    
    return password

    
