#open mode and create mode
# f1=open("file1.txt","x") # "x" is for create a file, open is for opening a new file

#read mode - (reading content of an exsisting file)
'''
f1=open("file1.txt","r")
print(f1.read())
'''
#if no mode is specified then python interpreter assumes it as read mode("r")
'''
f1=open("file1.txt")
print(f1.read())
'''

#opening a non exsisting file in read mode gives error
'''
f1=open("file2.txt")
print(f1.read())
'''

#write mode

#create a file if it already doesn't exists
# f2=open("file2.txt","w")

# remove exsisting content of an exsisting file i.e., overwrite
'''
f1=open("file1.txt","w")
f1.write("I am learning python")
print(f1.read())#gets error bcz it doesn't use "r"
'''
#"r+"- read + write mode(it doesn't overwrite existing content,instead it append new content with existing content)
'''
f1=open("file1.txt","r+")
print(f1.read())
f1.write("full stack")

'''
#"r+" - what if first write then read
'''
f1=open("file1.txt","r+")
print(f1.tell())
f1.write("full stack")
print(f1.tell())
print(f1.read())
print(f1.tell())
'''

#"w+"- write mode + read mode
#it overwrite if an already file contains any content
#create a new file if file name doesn't already exists 
'''
f1=open("file1.txt","w+")
f1.write("Gods own country")
print(f1.tell())
print(f1.seek(0))
print(f1.read())
'''

#"a"- append mode
#create a new file if file name doesn't already exists
'''
f1=open("file1.txt","a")
f1.write("beautiful")
'''

#"a+" - append + read
'''
f1=open("file1.txt","a+")
f1.write("hello")
f1.seek(0)
print(f1.read())

'''
#\n use
'''
f1=open("file3.txt","w")
f1.write("Hii kiran \n iam learning full stack python")
'''
#'\\' for opening with location
'''
f1=open("C:\\Users\\kiran\\Desktop\\file4.txt","r")
print(f1.read())
'''
#with out '\\' for opening with location
'''
f1=open(r"C:\Users\kiran\Desktop\file4.txt","r")
print(f1.read())

'''