def get_integer():
    return int(input("Give me a number: "))


def is_prime(number):
    if number % 2 == 0:
        return print("It is a prime number")
    else:
        return print("It is a odd number")


num = get_integer()
is_prime(num)
