import random


def list_end(a_list):
    return [a_list[0], a_list[-1]]


a = random.sample(range(100), 9)
print(a)
num = list_end(a)
print(num)
