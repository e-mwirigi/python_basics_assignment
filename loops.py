#Use a for loop to print numbers from 1 to 10.
for i in range(1,11):
    print(i, end= ', ')

print() # adding blank lines between outputs

#Use a while loop to print numbers until the user enters stop.
while True:
    user_input = input('> ')
    if user_input == 'stop':
        break
    print(user_input)

print() # adding blank lines between outputs

#Write a loop that prints even numbers from 1 to 20.
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end= ' ')

print() # adding blank lines between outputs

# Explain what break and continue do in your own words.
'''
1. The break key word when executed, forces exit of the loop immediately, regardless of whether
    the loop has iterated through all its items.
'''
'''
2. The continue key word when executed, skips the current iteration of a loop, and moves to the next iteration.
'''

print() # adding blank lines between outputs

#A guessing game that asks the user to guess a secret number between 1 and 10, Give feedback (too high / too low).
while True:
    user_guess = int(input('Enter a number between 1 and 10: '))
    if user_guess < 1:
        print('too low')
        continue
    elif user_guess > 10:
        print('too high')
        continue
    else:
        print(f"Your secret number is: {user_guess}")
        break
