import random

def number():

    while True:
        try:
            min_value = int(input("Enter the minimum value: "))
            max_value = int(input("Enter the maximum value: "))
            break
        except:
            print("Enter a number only")

    quit = "y"
    while True:
        random_number = random.randint(min_value, max_value)
        print(random_number)
        quit = str(input("Do you want to roll again? (y/n): "))
        if quit!="y":
            break


    print("Random number between", min_value, "and", max_value, "is:", random_number)

def alph():
    while True:
        lst = ['a', 'b', 'c', 'd', 'e']
        random_letter = random.choice(lst)
        lst.remove(random_letter)
        print(random_letter)
        quit = str(input("Do you want to roll again? (y/n): "))
        if quit!="y":
            break

def coin():
    while True:
        while True:
            choice = str(input("Choose heads or tails: "))
            if choice.lower() == 'heads' or choice.lower() == 'tails':
                break
            else:
                print("Invalid input. Please enter 'heads' or 'tails'.")   
        
        land = random.randint(1,2)
        if land == 1 and choice == "heads":
            print("Correct coin toss landed on heads")
        elif land == 2 and choice == "tails":
            print("Correct coin toss landed on tails")
        elif land == 1:
            print("Sorry cointoss landed on heads")
        else:
            print("Sorry coin toss landed on tails")

        quit = str(input("Do you want to roll again? (y/n): "))
        if quit!="y":
            break

yes = str(input("Do you want to roll dice? (y/n): "))
if yes.lower() == "y":
    number()
yes = str(input("Do you want to get a random alphabet? (y/n): "))
if yes.lower() == "y":
    alph()
yes = str(input("Do you want to toss a coin? (y/n): "))
if yes.lower() == "y":
    coin()