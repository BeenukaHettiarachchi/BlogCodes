# Swaping values


# Standard Method
a = 60
b = 90

c = a
a = b
b = c

print(f'a = {a}\nb = {b}')



# Pro Method
a = 60
b = 90


a, b = b, a

print(f'a = {a}\nb = {b}')