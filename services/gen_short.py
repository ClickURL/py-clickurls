import random
import string

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for i in range(6))
    return short_code
