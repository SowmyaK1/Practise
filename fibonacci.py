def get_integer(help_text):
    return int(input(help_text))


def fibonacci(num):
    x = 1
    if num == 0:
        f_seq = []
    elif num == 1:
        f_seq = [1]
    elif num == 2:
        f_seq = [1, 1]
    elif num > 2:
        f_seq = [1, 1]
        for x in range(num - 2):
            f_seq.append(f_seq[x] + f_seq[x + 1])
            x += 1
    return f_seq


num = get_integer("Enter the number of numbers in the sequence to generate: ")
y = fibonacci(num)

print(y)
