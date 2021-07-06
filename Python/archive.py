# Variables - Integers and floats
x_pos = 10 # integer 
y_pos = 20

print(x_pos + y_pos)

x_pos = 15

print(x_pos + y_pos)

pi = 3.14 # float
print(x_pos + y_pos * pi)

x_pos = 15.0
print(x_pos + y_pos * pi)
print(type(x_pos))

# Variables - Booleans and Strings
is_game_over = False
is_game_over = True

print(is_game_over)
print(type(is_game_over))

is_game_over = 1
print(is_game_over)
print(type(is_game_over))

name = "Jonas"
is_game_over_text = "False"
age_as_a_string = "5"
print(name)
print(type(name))

age = 33
name_and_age = "Jonas: {}".format(age)
print(name_and_age)

# Arithmetic operators -+*/ % // ** = 

x_pos = 10
forward = x_pos + 1
print(forward)
backward = x_pos - 1
print (backward)

remainder = 5 % 2
print(remainder)
floor_division = 5 // 2
print(floor_division)

five_squared = 5 ** 2
print(five_squared)

#x_pos = x_pos + 1 
x_pos += 1
print(x_pos)

first_name = "Jonas "
last_name = "Saxild"

print (first_name + last_name)

# operators you will be looking at
# > >= < <= == != not or and

x_position = 10
end_position = 10

# -- comparison operators -- #
# check if you are at end position
is_at_end = x_position == end_position
print(is_at_end)

# check if you are at halfway position
is_at_halfway = x_position >= end_position / 2
print(is_at_halfway)

# -- logical operators -- #
# not operator
not_is_at_end = not is_at_end
print(not_is_at_end)

# and operator
score = 10
# game is over if score is larger than 10 and position is at the end
is_game_over = score >= 10 and is_at_end
print(is_game_over)

# or operator
score = 9
# game is over if score is larger than 10 or position is at the end
is_game_over = score >= 10 or is_at_end
print(is_game_over)

# an example of a list
# name = [5, True, "string"]

# create a list of positions
enemy_positions = [5, 10, 15]

# reassign the list
enemy_positions = [5, 10, 15, 20]

print(enemy_positions)

# observe the length of the list
print(len(enemy_positions))

# access a single element in the list
print(enemy_positions[0])

# change the value at index 0 of the list
enemy_positions[0] = 6
print(enemy_positions)

# retrieve multiple elements of the list using slicing
print(enemy_positions[0:2])

# add an item to the end of the list
enemy_positions.append(25)
print(enemy_positions)

# insert an item at a specific index of the list
enemy_positions.insert(1,9)
print(enemy_positions)

# remove a specific item in the list
enemy_positions.remove(6)
print(enemy_positions)

# remove an item at a specific index of the list
del(enemy_positions[2])
print(enemy_positions)