import pickle
#write

#first create a binary file
'''
f1=open("bfile1.dat","wb")
my_list=["hi","full stack","python"]
my_tuple=(1,2,3,4,5)
my_dict={
    1:"kiran",
    2:"hello",
    3:"full satck"
}
pickle.dump(my_list,f1)
pickle.dump(my_tuple,f1)
pickle.dump(my_dict,f1)
'''

#read
#then read the created binary file
f2=open("bfile1.dat","rb")
ma_list=pickle.load(f2)
ma_tuple=pickle.load(f2)
ma_dict=pickle.load(f2)
print(ma_list,ma_tuple,ma_dict)