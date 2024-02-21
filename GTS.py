import random
print(" WELCOME :)")
print("------------")

num_limit = input("Enter the limit: ")

if num_limit.isdigit():
    num_limit = int(num_limit)

    if num_limit == 0:
        print("PLEASE ENTER A NUMBER LARGER THAN 0!")
        quit()
else:
    print("PLEASE ENTER A NUMBER NEXT TIME!")
    quit()
rand_num = random.randint(0,num_limit)
guesses = 0
while True:
    guesses += 1
    user_guess = input("MAKE A GUESS: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("PLEASE ENTER A NUMBER NEXT TIME!")
        continue
    if user_guess == rand_num:
        print("YOU GOT IT!")
        break
    elif user_guess > rand_num:
        print("YOU ARE ABOVE THE NUMBER!")
    else:
        print("YOU ARE BELOW THE NUMBER!")
print("YOU GOT IT IN",guesses,"GUESSES!")