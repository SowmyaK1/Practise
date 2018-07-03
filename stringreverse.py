def get_string(help_text):
    return input(help_text)


def str_reverse(string):
    y = string.split()
    y.reverse()
    return " ".join(y)


string = get_string("Enter a string to reverse: ")
x = str_reverse(string)

print(x)
