import random
import string


def get_random_string(length=4):
    letters = string.ascii_uppercase
    code = ''.join(random.choice(letters) for i in range(length))
    return code