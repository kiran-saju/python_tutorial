a=int(input("1st num")) #1
b=int(input("1st num")) #2

temp=a      #temp=10 and is empty    
a=b #b's value is assigned to a(a=20) and now b is empty
b=temp #b=10 now
print(a)
print(b)

#without temp
a=int(input("enter number")) #10
b=int(input("enter number")) #20
a=a+b #a=10+20(30)
b=a-b #30-20 (10)
a=a-b
print(a) #20
print(b)#10




