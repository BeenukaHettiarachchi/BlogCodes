# Challenge-04

def hasEven(nums: int) -> bool:
    for num in nums:
        if num % 2 == 0:
            print('True')
            break
    else:
        print('False')

x = [1, 3, 7, 9, 11]
y = [0,3,7,8,1,9,13]
z = [23,51,69,33,44]

hasEven(x)
hasEven(y)
hasEven(z)