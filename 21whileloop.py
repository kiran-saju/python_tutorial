#iterative stmts

#I)while

#1

'''
i=1
while i<=5:
    print("hello world")
    i=i+1
print("loop terminated")

'''

#2

'''
i=1
while i<=10:
    print(i)
    i=i+1
print("loop terminated")

'''

#3 (infinite loop)
'''
i=1
while i<=10:
    print(i)
'''

#4

'''
i=10
while i>=1:
    print(i)
    i=i-1
print("loop terminated")

'''

#5
'''
i=2
while i<=20:
    print(i ,"is even")
    i=i+2
print("loop terminated")
'''

#5(odd)
'''
i=1
while i<=20:
    print(i,"is odd")
    i=i+2
print("loop terminated")
'''

#6 (10 - 100)
'''
i=10
while i<=100:
    print(i)
    i=i+10
print("loop terminated")
'''

#7 (10 times hello world)
'''
i=1
while i<=10:
    print(i,"hello world")
    i=i+1
print("loop terminated")

'''

#8 (sum of natural nos)

'''
sum=0
i=1
while i<=10:
    sum=sum+i
    i=i+1  
print(sum)

'''

#9 (sum of natural nos)

'''
n=int(input("enter the sum"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1  
print(sum)

'''

#10 (factorial)
'''

i=1
fact=1
while i<=5:
    fact=fact*i
    i=i+1
print(fact)

#or

i=5
fact=1
while i>=1:
    fact=fact*i
    i=i-1
print(fact)

#or

i=int(input("enter number"))
fact=1
while i>=1:
    fact=fact*i
    i=i-1
print(fact)

'''

# 11 sum of n even nos

'''

n=int(input("enter a number"))
i=2
sum=0
while i<=n:
    sum=sum+i
    i=i+2
print(f" sum of even nos of {n} is",sum)

'''

# 12 sum of n odd nos

'''
n=int(input("enter a number "))
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+2
print(f" sum of odd nos of {n} is",sum)

'''

#13 mul table of 5

'''

n=int(input("enter number "))
i=1
while i<=10:
    print(f"{n} * {i} =",i*n)
    i=i+1

'''


#14 sq pf a number

'''
i=1
while i<=10:
    print(f"{i}*{i}=",i**2)
    i=i+1
'''