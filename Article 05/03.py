# any()

players = ["Emma Watson","Ana de Armas","Taylor Swift","Jennifer Lawrence"]
injured = [False,True,True,False]

# Normal Method
for i in injured:
    if i:
        print('Injured players — won\'t be able to play.')
        break
else:
    print('All players are fit — ready to play.')
    
# Pro Method
if any(injured):
    print('Injured players — won\'t be able to play.')
else:
    print('All players are fit — ready to play.')

# One line Pro Method
print('Injured players — won\'t be able to play.' if any(injured) else 'All players are fit — ready to play.')


# Example lists for any()
l1 = [0,0,1,0,0]
l2 = [0,0,0,0,0]
l3 = ['hi','bye','','welcome']
l4 = ['','','']
l5 = [[],[],[],[12,21,13,31],[]]

print(any(l1))
print(any(l2))
print(any(l3))
print(any(l4))