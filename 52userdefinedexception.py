#user defined exception

#1) raise Exception - for conditions with using if-else 
'''
def check(n):
    if n<0:
        raise Exception("u entered a -ve number")
    else:
        print(n)
n=int(input("enter a number"))
check(n)
'''

#2) assert - for conditions without using if-else 
'''
def check():
    n=int(input("enter a number"))
    assert n>0, "oops negative!"
    print(n*n)
check()

'''