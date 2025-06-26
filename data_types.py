# Print the type of 42, 3.14, and 'hello'.
print(type(42))                             #<class 'int'> 

print(type(3.14))                           #<class 'float'>

print(type('hello'))                        #<class 'str'>

# Convert a string '100' to an integer.
str_num = '100'
int_num = int(str_num)
print(type(int_num))                            #<class 'int'>

# Add an integer and a float together. What is the result?
int_num = 45
float_num = 60.876
print(int_num + float_num)                      # result is a float.

#What happens when you try to multiply a string by a number?
str_num = '500'
int_num = 3
print(str_num * int_num)                        # 500500500 - string is repeated n number of times.


# program that asks the user to enter two numbers as strings, converts them to integers/float and prints their sum and type
str_num1 = input('Enter a numner of your choice \n')
str_num2 = input('Enter a second number \n')

conv_num1 = float(str_num1.replace(',', ''))
conv_num2 = float(str_num2.replace(',', ''))

sum_result = conv_num1 + conv_num2

print(sum_result, type(sum_result))