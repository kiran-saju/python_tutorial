#for 
#add items into a list where condition is s>=5 and s<=25
'''
l1=[]
for i in range(1,6):
    s=int(input("items "))
    if s>=5 and s<=25:
        l1.append(s)    
    else:
        print("out of condition")
print(l1)

'''

#while
'''
l1=[]
i=1
while True:
    s=int(input("items "))
    if s>=5 and s<=25:
        l1.append(s)
        i=i+1    
    else:
        print("out of condition")
    if i>5:
        break
print(l1)
'''

#2) factors of a given number
'''
n=int(input("enter number "))
i=1
while i<=n:
    if n%i==0:
        print("factors are: ",i)
    i=i+1
'''
#or
'''
n=int(input("enter number "))
for i in range(1,n+1):
    if n%i==0:
        print("factors are: ",i)
'''    

#3) sum of a given number
'''
sum=0
n=int(input("enter a number ")) #123
while n>0:
    lastdigit=n%10  #3
    sum=sum+lastdigit #0+3
    n=n//10 #123//10= 12
print(sum)



'''
# calculates the sum of even digits and the product of odd digits in a number entered by the user.
'''
sum=0
prdt=1
n=int(input("enter a number "))
while n>0:
    digit=n%10
    if digit%2==0:
        sum=sum+digit
    else:
        prdt=prdt*digit
    n=n//10
print("sum of even number is ",sum)
print("product of odd number is ",prdt)

'''
        
#4)amstrong number
'''
sum=0
n=int(input("enter a number "))
dupe=n
x=str(n)
length=len(x)
print(length)
while n>0:
    digit=n%10
    sum=sum+digit**length
    n=n//10
if sum==dupe:
    print(dupe,"is amstrong number") 
else:
    print(dupe,"is not amstrong number") 

'''
#5) fibonacci number
'''
n=int(input("enter number"))
n1,n2=0,1
sum=0
if n<0:
    print("enter num greater than 0")
else:
    for i in range(0,n):
        print(sum, end=" ")
        n1=n2 #n1=1,0,1,1
        n2=sum #n2=0,1,1,2
        sum=n1+n2 #1+0=1,1,2,3
'''   
#6)product of digits of given number
''' 
n=int(input("enter the digit "))
prdt=1
while n!=0:
    prdt=prdt*(n%10)
    n=n//10
print("product of digits is ",prdt)

''' 

#7) square of digit of a given number

''' 
n=int(input("enter the digit "))
sum=0
while n!=0:
    rem=n%10
    sqr=rem**rem
    sum=sum+sqr
    n=n//10
print("sum of aquare of digits is ",sum)

''' 

#8) reverse of a given number

''' 
rev=0
n=int(input("enter a number "))
while n>0:
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
print(rev)

''' 
#9) given number is palindrome or not

''' 
rev=0
n=int(input("enter a number "))
temp=n
while n>0:
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
if(temp==rev):

    print("is palindrome")
else:
    print("not palindrome")
''' 

#10) total no of factors of a given number
''' 
n=int(input("enter number "))
count=0
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" " "\n")
        count+=1
print("no of factors =",count)
''' 
    