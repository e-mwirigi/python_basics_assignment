#Write a program that checks if a number is positive, negative, or zero.
def num_checker(x):
    if x < 0:
        print('number is negative')
    elif x > 0:
        print('number is positive')
    else:
        print('number is equal to zero')

num_checker(3)
num_checker(0)
num_checker(-15)

#Create a program that checks if someone is eligible to vote.
def check_age(n):
    if n < 18:
        print('You are underage!')
    else:
        print('Congrats, you are eligble to vote!')

check_age(17)
check_age(21)

#Write a program that takes 3 numbers and prints the largest one.
def largest_num(num1, num2, num3):
    print(max(num1, num2, num3))

largest_num(17,12,35)


#Practice combining and, or, not.


#Build a grading system: Input score (0–100), Output grade: A (90+), B (80–89), etc.
score  = int(input('Enter your score: '))
if score in range(0, 101):
    if score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    elif score >= 60:
        print('D')
    elif score >= 50:
        print('E')
    else:
        print('F')
else:
    print('Invalid input')