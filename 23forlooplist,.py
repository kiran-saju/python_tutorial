#1
'''
my_list=['python','java','.net','kotlin','c++']
for i in my_list:
    print(i)
'''

#2 sq of elements in list
'''
l1=[1,2,3,4]
for i in l1:
    print(f"sq of {i} is",i**2)

'''

#3 print even nos in list
'''
l2=[3,4,6,9,12,17,36,99,108]
for i in l2:
    if i%2==0:
        print("even nos in list are ",i)

'''
#4 print odd nos in list
'''

l3=[3,4,6,9,12,17,36,99,108]
for i in l2:
    if i%2!=0:
        print("odd nos in list are ",i)

'''

#5 (output in single line)
'''
s="python programming"
for i in s:
    print(i, end=" ")
'''
#6
'''
s1=[1,5,10,12,15]
for i in s1:
    print(i)
'''

#7 (count of vowels)
'''
count=0
s="python programming"
for i in s:
    if i in ('a','e','i','o','u'):
        count+=1
print(count)

'''   
#8 (count of consonents) 
'''   
count=0
s="python programming"
for i in s:
    if i not in ('a','e','i','o','u'):
        count+=1
print(count)    
'''   
#9 (count of consonents by user input) 
'''  
count=0
s=input("enter string")
for i in s:
    if i not in ('a','e','i','o','u'):
        count+=1
print(count)    
'''  
#10 (count of vowelss by user input) 
'''  
count=0
s=input("enter string ")
for i in s:
    if i  in ('a','e','i','o','u'):
        count+=1
print(count)    
'''  