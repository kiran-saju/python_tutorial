#arbitary or variable length

#Type-1-> Arbitary positional arguments(*args)

#problem
'''
def add(a,b):
    print(a+b)
add(5,4)
add(5,4,6)

'''
#solution
'''
def add(*num):
    sum=0
    for i in num:
        sum=sum+i
    print(sum)
    # print(type(num)) 
add(2,6,7,8,11,100)
add(5,10,100,150)
add(1,2,3,)
'''
'''
def sub(*subs):
    if not subs:
        return 0  # Handle the case with no arguments
    diff = subs[0]
    for i in subs[1:]:
        diff -= i
    print(diff)

sub(5, 1)       # Output: 4
sub(1, 2, 1)    # Output: -2

'''


