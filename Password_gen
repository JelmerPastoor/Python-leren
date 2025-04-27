import string
import secrets
import random
from zxcvbn import zxcvbn
import pprint, getpass, sys

alphabet = string.ascii_letters + string.digits

def shuffle(string):
    x = list(string)
    random.shuffle(x)
    x = ''.join(x)
    return x

def password_gen(length):
    type_input = input('Wil je naast cijfers en letters ook karakters in je wachtwoord? [Y/N]\n')
    if type_input == 'Y':
        letters_string = ''.join(secrets.choice(alphabet) for i in range(length//2))
        characters_string = ''.join(secrets.choice(string.punctuation) for i in range(length//2))
        password = letters_string + characters_string
    else:
        letters_string = ''.join(secrets.choice(alphabet) for i in range(length))
        password = letters_string
    password = shuffle(password)
    return password

def test_single_password(password):
    result = zxcvbn(password)
    print(f"Value: {result['password']}")
    print(f"Password Score: {result['score']}/4")
    print(f"Crack Time: {result['crack_times_display']['offline_slow_hashing_1e4_per_second']}")
    print(f"Feedback: {result['feedback']['suggestions']}")
    #pprint.pp(result)

password = password_gen(28)
print(password)
test_single_password(password)

# https://thepythoncode.com/article/build-a-password-manager-in-python