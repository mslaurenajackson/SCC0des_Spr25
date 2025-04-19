#user number guessing game

user_guess = int(input("Your guess: " ))

number_guess = user_guess #where the user guesses a number

number = 5
# the number that the user should guess is 5

while number == 5:

        if number < number_guess:

            print("Too high!")

        if number > number_guess:

            print("Too low!")

        if number == number_guess:

            print("Your guess is right!")

        break