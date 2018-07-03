num = int(input("Enter a number: "))

a = range(1, 100)
new_list = []

for x in a:
    if x % num == 0:
        new_list.append(x)

print("\n" + "Following are list of diviors of " + str(num))
print(new_list)
