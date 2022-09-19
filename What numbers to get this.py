import random


print("When choosing a number, choose one below 10,001!")
print("Please note, high or low numbers such as 0 and 10,000 will take a longer time to find calculations "
      "for it!")
user_operations = input("Operations: +, - , / , * ? ")
if user_operations == "+":
    user_number = input("What number you want?")
    while True:
        first = random.randint(0, 5000)
        second = random.randint(0, 5000)
        final_number = first + second
        if final_number == int(user_number):
            print(str(first) + " + " + str(second) + " = " + str(final_number))
if user_operations == "-":
    user_number = input("What number you want? ")
    while True:
        first = random.randint(0, 5000)
        second = random.randint(0, 5000)
        final_number = first - second
        if final_number == int(user_number):
            print(str(first) + " - " + str(second) + " = " + str(final_number))
if user_operations == "/":
    user_number = input("What number you want? ")
    while True:
        first = random.randint(1, 5000)
        second = random.randint(1, 5000)
        final_number = first / second
        if final_number == int(user_number):
            print(str(first) + " / " + str(second) + " = " + str(final_number))
if user_operations == "*":
    user_number = input("What number you want? ")
    while True:
        first = random.randint(0, 5000)
        second = random.randint(0, 5000)
        final_number = first * second
        if final_number == int(user_number):
            print(str(first) + " * " + str(second) + " = " + str(final_number))
