# List Filtering

x = [0,65,3,67,23,556,123,59,42,91,100,4,19,50]

y = [i for i in x if i >= 50]

print(y)

y = []
for i in x:
    if i >= 50:y.append(i)

print(y)