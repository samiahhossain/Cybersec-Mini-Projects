import random
import string

characters = list(" " + string.ascii_letters + string.digits + string.punctuation)
key = characters.copy()
# New key each time
random.shuffle(key)

message = input("Enter your message: ")
encoded = ''

for character in message:
    index = characters.index(character)
    encoded += key[index]

print(f"Encoded message: {encoded}")
print("Weakness of this method: the same letter is encoded the same throughout the message, so frequency analysis and brute force can be used to help decipher.")