import datetime
now = datetime.datetime.now()
# print now.year

name = input("What's your name? ")
print("Nice to meet you " + name + "!")

age = int(input("Your age? "))
current_year = now.year
year = int(100 - age + current_year)

times = int(input('How many times do you want to print? '))

print ("So, you will be 100 years old in " + str(year) + "  " + name + "!") * times

