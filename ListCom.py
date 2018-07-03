a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 102, 150, 167, 189, 175, 196, 200]

# Even_List = []

# for i in a:
#     if i % 2 == 0:
#         Even_List.append(i)

Even_List = [i for i in a if i % 2 == 0]

print("List of even numbers in list are ")
print(Even_List)
