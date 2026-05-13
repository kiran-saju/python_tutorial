#1
'''
for i in range(1,5):
    for j in range(1,4):
        print(f"i's {i}","  "f"j's {j}")

'''

#2

'''
for i in range(1,5):
    for j in range(1,4):
        print(i,j,end=" ")
    print()
'''

#3

'''
for i in range(1,11):
    for j in range(1,11):
        print(f"{i}*{j}= ",i*j,end="")
    print()

'''
#4
'''
for i in range(1,6):
    for j in range(1,10):
        print(j, end=" ")
    print()
'''

#5
'''
for i in range(1,6):
    for j in range(1,6):
        print('*', end=" ")
    print()
'''
#6
'''
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end=" ")
    print()
'''
#7
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

'''
#8
'''
for i in range(1,6):
    for j in range(i):
        print(i-j, end=" ")
    print()
'''
#9
'''
for i in range(1,6):
    for j in range(6-i):
        print('*', end=" ")
    print()
'''

#10
'''

for i in range(1,6):
    for j in range(6-i):
        print(j+1, end=" ")
    print()

'''

#or

'''
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
'''