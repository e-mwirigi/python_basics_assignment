# Create a list of 5 fruits and print the third fruit
fruits = ['Mango', 'Orange', 'Peach', 'Apple', 'Kiwi']
print(fruits[2])

# Create a dictionary with keys: name, age. Print the value of age.
voter = {
    'name': 'Kent',
    'age': 35
}
print(voter['age'])

# Define a tuple with three numbers. Try modifying it. What happens?
num_tuple = ('5', '24', '76')

#num_tuple[1] = '37'
print(num_tuple, type(num_tuple))       # TypeError: 'tuple' object does not support item assignment
                                        # because tuples are immutable and do not allow element changes.


# Create a set from a list with duplicate values.
my_list = ['45', '45', '67', '76', '76', '90']
my_set = set(my_list)
print(my_set)

# A program that takes 5 user inputs and stores them in a list, Converts the list into a set and prints the unique values
new_list = []
for i in range(5):
    item = input(f"Enter item {i + 1} of 5: ")
    new_list.append(item)

new_set = set(new_list)
print(new_set)