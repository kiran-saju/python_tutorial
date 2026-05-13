#1
'''

l1=[]
length=int(input("length "))
for i in range(length):
    s=int(input("items "))
    l1.append(s)
print(l1)

'''
#2

'''
l1=[]
length=int(input("length "))
for i in range(length):
    s=input("items ")
    l1.append(s)
print(l1)

'''
#3

'''

l2=[]
sum=0
total_elements=int(input("no of elements"))
for i in range(total_elements):
    m=int(input("measurements in cms "))
    l2.append(m)
print(l2)  
for i in l2:
    sum=sum+i
    average=sum/total_elements
print("average is ",average)
'''

#4

''' 
n=int(input("enter a number"))
for i in range(n+1):
    if((i%5==0) and (i%3==0)):
        print("fizzbuzz")
    elif(i%3==0):
        print("buzz")
    elif(i%5==0):
        print("fuzz")
    else:
        print(i)
'''
#5(max value in list)
'''
l1=[]
length=int(input("length "))
for i in range(length):
    s=int(input("items "))
    l1.append(s)
print(l1)
max_value=l1[0] 
for i in l1:
    if i>max_value:
        max_value=i
print("maximum value is ",max_value)
'''
#6(sq of elements in list)

'''
l1=[]
length=int(input("length "))
for i in range(length):
    s=int(input("items "))
    l1.append(s)
print(l1)
l2=[]
for i in l1:
    sq=i**2
    # print(sq)
    l2.append(sq)
print(l2)

'''