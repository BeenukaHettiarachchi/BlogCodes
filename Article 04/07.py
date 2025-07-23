# Enumerate with index

the_list = ['Python','Java','C++','Ruby','Dart']

# Standard Method

c = 1
for lang in the_list:
    print(f'{c}. {lang}')
    c += 1

# Pro Method

for index,lang in enumerate(the_list,1):
    print(f'{index}. {lang}')
    
