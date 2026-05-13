#hw1
 
'''
a=int(input("1st number "))
b=int(input("2nd number "))
res=input(" +,-,*,% ")
if(res=='+'):
    print("sum is ", a+b)
elif(res=="-"):
        print("difference is ",a-b)
elif(res=="*"):
       print("mul is ",a*b)
elif(res=="/"):
       print("div  is ",a/b)
   
elif(res=="%"):
       print("modulus is ",a%b)
else:
    print("invalid ops")
'''
    
#hw2


'''
a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
if(a>b):
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is greater than {a}")
'''

#hw3

'''
a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
if(a>b and a>c):
    print(f"{a} is greater than {b} and {c}")
elif(b>a and b>c):
    print(f"{b} is greater than {a} and {c}")
else:
    print(f"{c} is greater than {a} and {b}")

'''

#hw4 

'''
a=int(input("enter a number"))
if(a%2==0 and a%3==0):
    print(f"{a} is divisible by both 2 and 3")

elif(a%2==0 and a%3!=0):
        print(f"{a} is divisible by 2 and not divisible by 3")

elif(a%2!=0 and a%3==0):
     print(f"{a} is divisible 3 and not divisible by 2")

else:
     print("invalid condition")

'''

#hw5(right angle)

'''
b=int(input("enter base"))
a=int(input("enter altitude"))
h=int(input("enter hypotenous"))
h_sq= h**2
b_sq= b**2
a_sq= a**2
if (a_sq + b_sq == h_sq): 
    print("it is right angle")

elif (a_sq+ b_sq== h_sq):
     print("it is right angle")    
else:
     print("it is not right angle")

'''


#hw6 (prove traingle is equilateral, isosceles and scalar)

'''
a=int(input("enter 1st side"))
b=int(input("enter 2nd side"))
c=int(input("enter 3rd side"))
if(a==b==c):
    print("equilateral triangle")
elif((a==b or a==c) or (b==a or b==c) or (c==a or c==b)):
    print("isosceles triangle")
else:
    print("scalane traingle")
'''

#hw7 (pizaa bill)


size = input("enter size - s/m/l ")
price=0
if(size=='s'):
    price+=100
    print("price is ",price)
    peperonit=input("do u want peperonit; yes/no ")
    if(peperonit=='yes'):
        price+=50
        print("price is ",price)
    elif(peperonit=='no'):
        price=price
        print("price is ",price)
    else:
        print("invalid option for peperonit")

    extracheese=input("do u want extra cheese ")
    if(extracheese=='yes'):
        price+=20
        print("price is ",price)
    elif(extracheese=='no'):
        price=price
        print("price is ",price)
    else:
        print("invalid option for extra cheese")

elif(size=='m'):
    price+=200
    print("price is ",price)
    peperonit=input("do u want peperonit; yes/no ")
    if(peperonit=='yes'):
        price+=70
        print("price is ",price)
   
    elif(peperonit=='no'):
        price=price
        print("price is ",price)
    else:
        print("invalid option for peperonit")
    extracheese=input("do u want extra cheese ")
    if(extracheese=='yes'):
        price+=20
        print("price is ",price)
    elif(extracheese=='no'):
        price=price
        print("price is ",price)
    else:
        print("invalid option for peperonit")
       
          
elif(size=='l'):
    price+=300
    print("price is ",price)
    peperonit=input("do u want peperonit; yes/no ")
    if(peperonit=='yes'):
        price+=70
        print("price is ",price)
   
    elif(peperonit=='no'):
        price=price
        print("price is ",price)
    else:
        print("invalid option for peperonit")
    extracheese=input("do u want extra cheese ")
    if(extracheese=='yes'):
        price+=20
        print("price is ",price)
    elif(extracheese=='no'):
        price=price
        print("price is ",price)
    else:
        print("invalid option for peperonit")
            
else:
    print("invalid option")


#hw8 (login)

'''
import sys
username=input("enter username ")
if(username=='kiran'):
    print("username is correct")
    password=input("enter password")
    if(password=='555'):
        print("passsword is correct")
    else:
        password=input("wrong password, re-enter password: ")
        if(password=='555'):
           print("passsword is correct")
        else:       
             print("chance over")
             sys.exit()
    email=input("enter email: ")
    if('@' not in email):
        print("'@' must included")
        email=input("enter email: ")
        
        if(email=='kiran@'):
            print("email is registered")
        else:
            print("chance over email is not registered") 
    else:
        print("email is not registered")
else:
    print("invalid username")

'''