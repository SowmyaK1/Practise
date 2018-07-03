import random
import string


def PasswordGenerator(size=8, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))


print(PasswordGenerator(int(input('How many characters in your password? '))))
