#Write a function greet(name) that prints “Hello, [name]”.
def greet(name):
    print(f'Hello, {name}.')

greet('Alexander')

#Create a function add(a, b) that returns the sum.
def add(a,b):
    return a+b

print(add(17,18))

#Modify add() to print “even” or “odd” based on the result.
def add(a,b):
    result = a+b
    if result % 2 == 0:
        print(f'{result}, even')
    else:
        print(f'{result}, odd')

add(18, 5)
add(57, 13)

#Call a function from within another function.
def square(num):
    return num ** 2

def sum_of_squares(num1, num2):
    sum = square(num1) + square(num2)
    return sum

print(sum_of_squares(6,9))

#Calculator function that Takes two numbers and an operation (+, -, *, /), and returns the result
def calc_func(n1, n2, operation):
    if operation == '+':
        return n1+n2
    elif operation == '-':
        return n1-n2
    elif operation == '*':
        return n1*n2
    elif operation == '/':
        if n2 == 0:
            return 'Zero division not allowed.'
        else:
            return n1/n2
    else:
        return 'invalid operation'

print(calc_func(3,0, '/'))
print(calc_func(6,9, '*'))
print(calc_func(11.3,5, '-'))
print(calc_func(7,4, '+'))
