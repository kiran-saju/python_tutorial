import pickle
f1=open("samp1.dat", "wb")
my_list=["Tiger","Lion","Jaguor"]
#converting list to binary
pickle.dump(my_list,f1)

#converting tuple to binary
f2=open("samp2.dat", "wb")
my_tuple=(1,2,3)
pickle.dump(my_tuple,f2)

#converting dict to binary
f3=open("samp3.dat", "wb")
my_dict={
    "h":1,
    "j":2
}
pickle.dump(my_dict,f3)