# Reversing a  list

the_list = ['I','Love','You']

# Standard way
reversed_list = []

for word in the_list:
    reversed_list = [word] + reversed_list
    
print(reversed_list)

# Pro Method

print(the_list[::-1])