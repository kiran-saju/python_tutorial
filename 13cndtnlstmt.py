# if 
'''
age=int(input("Enter your Age"))
if age<=3:
    print("token not required")
'''
    
# if-else

'''
number = int(input("enter the number"))
if number%2==0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
'''

#elif

'''
color = input("enter the color ").capitalize()
if(color=="Red"):
    print("Stop")
elif(color=="Yellow"):
    print("Get Ready")
elif(color=="Green"):
    print("GO")
else:
    print("Invalid Input")

'''
#cw1
'''
number1 = int(input("enter first number"))
number2 = int(input("enter second number"))
difference= number1-number2
if(difference<0):
    print((difference*-1))
else:
    
    print(difference)
'''
#or
'''
number1 = int(input("enter first number"))
number2 = int(input("enter second number"))
if(number1>number2):
    print(number1-number2)
else:
    print(number2-number1)
'''

#cw2
'''
mark = int(input("enter mark"))
if(mark>=90 and mark<=100):
    print("Out Standing")
elif(mark>=80 and mark<=89):
    print("excellent")
elif(mark>=70 and mark<=79):
    print("very good")
elif(mark>=60 and mark<=69):
     print("good")
elif(mark>=50 and mark<=59):
    print("try hard")
else:
    print("Invalid Input")
'''

#cw3

'''
number=int(input("enter number "))
if(number<0):
    print(f'{number} is -ve')
elif(number==0):
    print(f'{number} is Zero')
else:
    print(f'{number} is +ve')
'''

#cw4
'''
number=int(input("enter number "))
if((number>=50 and number<=99) and (number%2==0)):
    print(f'{number}  is greater than 50 and is even')
elif((number>=50 and number<=99) and (number%2!=0)):
    print(f'{number} is greater than 50 and it is  odd')
elif((number>=100 and number%2==1)):
    print(f'{number} is greater than 100 and it is  odd')
elif((number>=100 and number%2==0)):
    print(f'{number} is greater than 100 and it is  even')
else:
    print(f'{number} is lesser')

'''

#Nested If

'''
number=int(input("enter number "))
if(number%2==0):
    print(f"{number} is +ve")
    if(number>=50 and number<=99):
        print(f"{number} is larger than 50")
    elif((number%2==1) and (number>=100)):
        print(f"{number} is larger than 100")
else:
    print("less")

'''


#cw 5

'''
import sys
height=int(input("enter your height in feets"))

if(height>=3):
    age=int(input("enter age "))
    cost=0
    if(age>=9 and age<=12):
        cost=100
        print(cost)
    elif(age>=13 and age<=18):
        cost+=100
        print(cost)
    elif(age>=19 and age<=21):
        cost+=200
        print(cost)
    elif(age>=22 and age<=55):
        cost+=300
        print(cost)
    else:
        print("below age ")
        sys.exit()
    click=input("do you want a click? yes/no ")
    if(click=='yes'):
        cost+=50
        print(cost)
    elif(click=='no'):
        cost=cost
        print(cost)
    else:
        print("Invalid input")

else:
    print("u r below 3 feets")

    '''

'''
year=int(input("enter the year "))
if(year%4==0):
    # print("leap year")
    if(year%100!=0):
         print("leap year")
    elif(year%400==0):
        print("leap year")

    elif(year%400!=0):
         print("not leap")
        
else:
    print("not aleap year")

    '''

#or

'''

year=int(input("enter the year "))
if(year%4==0):
    # print("leap year")
    if(year%100==0):
         
         
        if(year%400==0):
          print("leap year")

        else:
            print("not a leap year")
    else:
       print("not leap year")
        
else:
    print("not aleap year")

'''
#or
'''

year=int(input("enter the year "))
if((year%4==0 and year%100!=0) or (year%400==0)):
    print("leap year")
else:
    print("not leap year")

'''

