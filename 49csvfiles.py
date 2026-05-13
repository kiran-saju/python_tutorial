#with 'x' - creating a csv file
'''
f1=open("sample.csv","x")
'''
#with 'w' - create, write,overwrite

'''
import csv
f1=open("sample.csv","w",newline="")
s_write=csv.writer(f1,delimiter=":")
s_write.writerow(["RollNo","Name","Movies"])
rec=[] #for storing list values
while True:
    r=int(input("enter roll no"))
    n=input("enter name")
    m=int(input("enter marks"))
    my_list=[r,n,m]
    rec.append(my_list)
    choice=input("do u want to enter another data? y/N")
    if choice=="n":
        break
for i in rec:
    s_write.writerow(i)
'''

#without using for loop(writerows)

import csv
f1=open("sample.csv","w",newline="")
s_write=csv.writer(f1)
s_write.writerow(["RollNo","Name","Movies"])
rec=[] #for storing list values
while True:
    r=int(input("enter roll no"))
    n=input("enter name")
    m=int(input("enter marks"))
    my_list=[r,n,m]
    rec.append(my_list)
    choice=input("do u want to enter another data? y/N")
    if choice=="n":
        break
s_write.writerows(rec)
f1.close()

#read csv file
f1=open("sample.csv","r")
s_reader=csv.reader(f1)
for i in s_reader:
    print(i)
f1.close()

#append
f1=open("sample.csv","a",newline="")
s_write=csv.writer(f1)
# s_write.writerow(["RollNo","Name","Movies"])
rec=[] #for storing list values
while True:
    r=int(input("enter roll no"))
    n=input("enter name")
    m=int(input("enter marks"))
    my_list=[r,n,m]
    rec.append(my_list)
    choice=input("do u want to enter another data? y/N")
    if choice=="n":
        break
s_write.writerows(rec)
f1.close()


