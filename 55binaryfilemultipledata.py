#entering multiple data in a binary file
import pickle
'''
f1=open("sam4.dat","wb")
while True:
    roll_no=int(input("roll no"))
    name=(input("name"))
    age=int(input("age"))
    my_rec=[roll_no,name,age]
    pickle.dump(my_rec,f1)
    choice=input("do u want to enter another data?, y/n")
    if choice=="n":
        break

'''
f1=open("sam4.dat","rb")
try:
    while True:
        my_rec=pickle.load(f1)
        print(my_rec)
except EOFError:
    f1.close()