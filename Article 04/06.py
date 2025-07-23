# Join list of strings

the_list = ['I','love','you']


# Standard method
final_str = ''
for word in the_list:
    final_str = final_str + word + ' '
    
print(final_str)

# Pro Method
pro_str = ' '.join(the_list)
print(pro_str)