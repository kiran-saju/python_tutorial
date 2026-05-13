#1)
'''
for i in range(1,6):
    # print(i,end=" ")
    for j in range(1,10):
        print(j,end=" ")
    print()
'''
#2)
'''
for i in range(1,5):
    for j in range(1,5):
        print("*",end=" ")
    print()
'''
#3) basic triangle
'''
for i in range(1,6):
    for j in range(1,i+1):
          print("*",end=" ")
    print()
'''
#or
'''
for i in range(6,1,-1):
    for j in range(6,i-1,-1):
        print("*",end=" ")
    print()
'''
#4) inverse of basic triangle
'''
for i in range(1,6):
    for j in range(i,6):
        print("*",end=" ")
    print()
#or
for i in range(1,6):
    for j in range(6,i,-1):
        print("*",end=" ")
    print()
'''
#5
'''
for i in range(1,6):
    for j in range(5,i,-1):
        print("#",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()
'''
#6
'''
for i in range(1,6,1):
    for j in range(1,i,1):
        print(" ",end=" ")
    for k in range(6,i,-1):
        print("*",end=" ")
    print()
'''
#7)pyramid
'''
for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    for l in range(1,i):
          print("*",end=" ")
    print()
'''
#8)
'''
for i in range(1,5):
    for j in range(1,i+i):
        print("*",end=" ")
    print()
'''
#9) inverse pyramid
'''
for i in range(1,6):
    for j in range(i-1):
        print(" ",end=" ")
    for k in range(6,i,-1):
        print("*",end=" ")
    for l in range(6,i+1,-1):
        print("*",end=" ")
    print()
'''

#10)Number pattern
'''
p=1
for i in range(1,6): #row
    for j in range(1,6): #col
        print(p,end=" ")
    print()
    p+=1
'''
#11)
'''
p=1
for i in range(1,6):
    for j in range(i):
        print(p,end=" ")
    print()
    p=p+1
'''
#12)
'''
p=1
for i in range(1,6):
    for j in range(i-1):
        print(" ",end=" ")
    for k in range(6,i,-1):
        print(p,end=" ")
    print()    
    p=p+1
'''
#13)
'''
p=5
for i in range(1,6):
    for j in range(i-1):
        print(" ",end=" ")
    for k in range(6,i,-1):
        print(p,end=" ")
    print()
    p=p-1
'''

#14)
'''
p=1
for i in range(1,6):
    for j in range(6,i+1,-1):
        print(" ",end=" ")
    for k in range(i):
        print(p,end=" ")
    for l in range(i-1):
        print(p,end=" ")
    print()
    p=p+1
'''
#15) even num pyramid
'''
p=0
for i in range(1,6):
    for j in range(i):
        print(p,end=" ")
    print()
    p=p+2
'''
#or
'''
p=0
for i in range(1,6):
    for j in range(i):
        print(p+p,end=" ")
    print()
    p=p+1
'''
#16)
'''
for i in range(1,6):
    for j in range(i):
            if i%2==0:
                print(2,end=" ")
            elif i%2==1:
                 print(1,end=" ")
            else:
                 print("nothing")
    print()
'''
#17)hetrogenous number pattern
'''
for i in range(1,6):
    p=1
    for j in range(1,i+1):
        print(p,end=" ")
        p=p+1
    print()
'''
#18)
'''
for i in range(1,6):
    p=1
    for j in range(i-1):
        print(" ",end=" ")
    for k in range(6,i,-1):
        print(p,end=" ")
        p=p+1
    print()

''' 
#19)hetrogenous pyramid
''' 
for i in range(1,6):
    p=1
    for j in range(6,i,-1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(p,end=" ")
        p=p+1
    for l in range(1,i):
        print(p,end=" ")
        p=p+1
    print()
''' 
#20) combined pyramid
''' 
for i in range(1,5):
    for j in range(5,i,-1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
        
    for l in range(1,i):
        print("*",end=" ")  
    print()
for m in range(1,6):
    for n in range(m-1):
        print(" ",end=" ")
    for o in range(6,m,-1):
        print("*",end=" ")
    for p in range(6,m+1,-1):
        print("*",end=" ")
    print()
''' 
#hw)
'''
p=5
for i in range(1,6):
    for j in range(i):
        print(p,end=" ")
    print()
    p=p-1
'''
#heart pattern
'''
for i in range(6,10):
    for j in range(i):
        print("*",end=" ")
    for k in range(9,i,-1):
        print(" ",end=" ")
    for k in range(9,i,-1):
        print(" ",end=" ")
    for l in range(i):
        print("*",end=" ")
    print()
   
for m in range(1,10):
    for n in range(m-1):
        print(" ",end=" ")
    for o in range(10,m,-1):
        print("*",end=" ")
    for p in range(10,m+1,-1):
        print("*",end=" ")
    print()
'''

#hollow patterns

#1
'''
for i in range(1,6):
    for j in range(1,6):
        if j==1 or j==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#2
'''
for i in range(1,6):
    for j in range(1,6):
        if j==1 or j==5:
            print("*",end=" ")
        elif i==1 or i==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#3
'''
for i in range(1,6):
    for j in range(1,6):
        if j==1 or i==5 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#4
'''
for i in range(1,6):
    for j in range(1,6):
        if i==6//2 or j==6//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#5
'''
for i in range(1,6):
    for j in range(1,6):
        if i==j or i+j==6:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#6
'''
for i in range(1,6):
    for j in range(1,6):
        if j==1 or i==1 or i+j==6:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#7
for i in range(1,6):
    for j in range(1,6):
        if i==5 or i+j==6 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(1,6):
        if i==5  or i==j :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#character pattern
#A-Z->65-90 and a-z-> 97-122

#1)
'''
p=89
for i in range(1,6):
    for j in range(i):
        print(chr(p),end=" ")
    print()
'''

#2)
'''
p=65
for i in range(1,6):
    for j in range(i):
        print(chr(p),end=" ")
    print()
    p+=1
'''

#3)
'''

p=69
for i in range(1,6):
    for j in range(i):
        print(chr(p),end=" ")
    print()
    p-=1
'''

#4)
'''
p=65
for i in range(1,6):
    for j in range(i):
        print(chr(p),end=" ")
    print()
    p+=2
'''
#5)
'''
p=65
s=66
for i in range(1,6):
    for j in range(i):
        if i%2==0:
            print(chr(s),end=" ")
        else:
            print(chr(p),end=" ")
    print()
'''
#6)
'''
p=65   
for i in range(1,5):
    for j in range(5,i,-1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(chr(p),end=" ")    
    for l in range(1,i):
        print(chr(p),end=" ")  
    print()
    p+=1
s=69
for m in range(1,6):
    for n in range(m-1):
        print(" ",end=" ")
    for o in range(6,m,-1):
        print(chr(s),end=" ")
    for p in range(6,m+1,-1):
        print(chr(s),end=" ")
    print()
    s-=1
'''
#7)
'''
p=65   
for i in range(1,5):
    for j in range(5,i,-1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(chr(p),end=" ")    
    for l in range(1,i):
        print(chr(p),end=" ")  
    print()
    p+=1
s=69
for m in range(1,6):
    for n in range(m-1):
        print(" ",end=" ")
    for o in range(6,m,-1):
        print(chr(s),end=" ")
    for p in range(6,m+1,-1):
        print(chr(s),end=" ")
    print()
    s+=1
'''

#8)different column values pattern
'''
for i in range(1,6):
    p=65
    for j in range(1,i+1):
        print(chr(p),end=" ")
        p+=1
    print()
'''
#9)  
''' 
for i in range(1,6):
    p=65
    for j in range(i-1):
        print(" ",end=" ")
    for k in range(6,i,-1):
        print(chr(p),end=" ")
        p=p+1
    print()
'''
#10)
'''
for i in range(1,6):
    p=69
    for j in range(i):
        print(chr(p),end=" ")
        p-=1
    print()
'''
#11)
'''  
for i in range(1,6):
    p=65 
    for j in range(6,i,-1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(chr(p),end=" ")  
        p+=1  
    for l in range(1,i):
        print(chr(p),end=" ")
        p+=1
    print()
''' 
