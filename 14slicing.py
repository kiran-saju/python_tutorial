s='python' 
#  012345
#p
print(s[0])
#py
print(s[0:2])
#pyt
print(s[0:3])
#thon
print(s[2:6])
print(s[2:])

#start stop step
print(s[0:6:1])
#pto
print(s[0:5:2])
print(s[0::2])
#ph
print(s[0:5:3])
#python
print(s[0::])


a=' p y t h o n '
# 0123456789101112
print(len(a)) #13

#get- p y t
print(a[0:6])

#(get-pyt)
print(a[1:7:2])

#(get-p y t h o)
print(a[1:11:1])

#(get-python)
print(a[1:12:2])


#negative slicing
s="python"
#  654321

#noh (by default step is -1)
print(s[-1:-4:-1]) 

#nohtyp
print(s[::-1])
print(s[-1:-7:-1])
print(s[-1::-1])



#palindrome
'''pal=input("enter word ")
a=pal[0::]
b=(pal[-1::-1])
if(a==b):
    print("palindrome")
else:
    print("not palindrome")
'''
