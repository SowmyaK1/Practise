import random

list1 = random.sample(range(100), 9)
list2 = random.sample(range(100), 8)

list3 = [x for x in list1 for y in list2 if x != y]

print(list1)
print(list2)
print(list3)
