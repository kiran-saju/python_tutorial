#break 1
'''
for i in range(1,11):
    print(i)
    if i==7:
        break
print("Force stopped")

'''
#break 2
'''

for i in range(1,11):
    if i==7:
        print(i, " in if block")
        break
    else:
        print(i, " in else block")
'''
#3 chocolate vending machine
'''
max_item=10
n=int(input("no of chocolates wanted"))
for i in range(1,n+1):
    if i>max_item:
        print("out of stock",i)
        break
    else:
        print("chocolate",i)
print("end")
'''
#4 chocolate vending machine(with out break)
'''
max_item=10
n=int(input("no of chocolates"))
for i in range(1,n+1):
    if i<=max_item:
        print("chocolate",i)
    else:
        print("out of stock",i)
'''

#5 prime number using for-else
num = int(input("enter a number"))
# Negative numbers, 0 and 1 are not primes
if num > 1:
  
    # Iterate from 2 to n // 2
    for i in range(2, (num//2)+1):
      
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")



#6 for-else
'''
for i in range(1,6):
    print(i)    
else:
    print("bye")
'''

#7
'''
s="python"
for i in s:
    print(i)
    if i=='h':
        break
'''
#8
'''
sum=0
l1=[]
length=int(input("length "))
for i in range(length):
    s=int(input("items "))
    l1.append(s)
    sum=sum+l1[i]
    if s<0:
        break 
else:
    print("list is ",l1)
    print("sum is ",sum)
'''   
