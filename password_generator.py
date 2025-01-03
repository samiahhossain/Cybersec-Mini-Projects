import random
import string

def generate():
    length = random.randint(8, 12)

    # Ensuring required chracters included
    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special_char = random.choice(string.punctuation)

    required = uppercase + lowercase + digit + special_char

    # Filling in the rest of the length with random characters
    characters = string.ascii_letters + string.digits + string.punctuation
    remaining = ''.join(random.choice(characters) for i in range(length - len(required)))

    # Join and mix so required ones are no longer just in the front
    password = list(required + remaining)
    random.shuffle(password)
    password = ''.join(password)

    return password

print(f"Here is a strong password: {generate()}")