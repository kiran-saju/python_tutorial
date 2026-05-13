#iterative stmts

#II)for loop

#1
'''
for i in range(6):
    print(i,"hello world!")#6 times hello world
'''

#or 
'''
for i in range(1,6,1):
    print("hello world!")#5 times hello world
    
'''

#2

'''
for i in range(1,11,1):
    print(i,"hello world!")

'''
#3 (even)

'''
for i in range(2,20,2):
    print(i," is an even number")

    '''

#4 (odd)

'''
for i in range(1,20,2):
    print(i, "is an odd number")

    '''
#4 (10 - 1)

'''
for i in range(10,0,-1):
    print(i)
'''

#5(10-100)
'''
for i in range(10,110,10):
    print(i)

'''

#6 (sum of 1 to 10)


'''
sum=0
for i in range(1,11,1):
    sum=sum+i
print(sum)


'''   

#7 (sum of 1 to n  by user input)

'''
n=int(input("number "))
sum=0
for i in range(1,n+1,1):
    sum=sum+i
print(sum)

'''

#8 (1 to 10)

'''
n=int(input("number "))
for i in range(1,n+1,1):

    print(i)

'''
#9 (sum of 1 to 10)

'''
sum=0
n=int(input("number "))
for i in range(1,n+1,1):
    sum=sum+i
    print(f"sum of {i} is ",sum)

'''
#10 (sum of first n even nos)

'''

sum=0
n=int(input("number "))
for i in range(0,n+1,2):
    sum=sum+i
    print(f"sum of {i} is ",sum)

'''

#11 (sum of first n odd nos)

'''

sum=0
n=int(input("number "))
for i in range(1,n+1,2):
    sum=sum+i
    print(f"sum of {i} is ",sum)

'''

#12 (mul of 5)

'''
n=10
m=5
for i in range(1,n+1,1):
    print(f"5*{i}=",m*i)

'''
#13 (mul of table by user input)

'''

m=int(input("number"))
n=10
for i in range(1,n+1,1):
    print(f"{m}*{i}=",m*i)

'''  
#14 (fact of num)
''' 
fact=1
for i in range(5,0,-1):
    fact=fact*i
print(fact)
''' 
#15 (fact of num by user input)
''' 
fact=1
n=int(input("number "))
for i in range(n,0,-1):
    fact=fact*i
print(fact)
''' 
#16 (sq of 1 to 10)
'''
for i in range(1,11,1):
    print(f"square of {i} is ",i**2)
'''
#17 (sq of 1 to 10 by user input)
'''
n=int(input("enter a number "))
for i in range(1,n+1,1):
    print(f"square of {i} is ",i**2)
'''
#18 (cube of 1 to 10)

'''
for i in range(1,11,1):
    print(f"cube of {i} is ",i**3)
'''

#19 (cube of 1 to 10 by user input)

'''
n=int(input("enter a number "))
for i in range(1,n+1,1):
    print(f"cube of {i} is ",i**3)
'''