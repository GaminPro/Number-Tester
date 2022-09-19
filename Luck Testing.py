import random


def main():
    number = input("Test Your Luck! Pick any number from 0 to 9! ")
    if number == "y":
        exit()
    if int(number) > 9:
        exit()
    lucky_number = random.randint(0, 9)
    if int(number) == lucky_number:
        print("You are quite lucky!")
        print("Winning number was " + str(lucky_number))
    else:
        print("Better luck next time!")
        print("Winning number was " + str(lucky_number))


while True:
    main()
    print("Press y to stop! ")
