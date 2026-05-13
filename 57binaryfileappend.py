#printing output in a nested list 

import pickle

f1=open("sam5.dat","wb")
details=[]
while True:
    roll_no=int(input("roll no"))
    name=(input("name"))
    age=int(input("age"))
    my_rec=[roll_no,name,age]
    details.append(my_rec) 
    choice=input("do u want to enter another data?, y/n")
    if choice=="n":
        break
pickle.dump(details,f1) 

f1=open("sam5.dat","rb")
data=pickle.load(f1)
print(data)

