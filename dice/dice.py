import random
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
