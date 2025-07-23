#Reversing a String

# Standard Method
the_string = 'Unboxed Articles'

reversed_string = ''

for char in the_string:
    reversed_string = char + reversed_string

print(reversed_string)

# Pro Method

print(the_string[::-1])