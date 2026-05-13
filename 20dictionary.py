#key-value pair, ordered, heterogenous, mutable
#key should be unique

my_dict={
  1:'lion',
  2:'tiger',
  3:'jaguar',
  4:'cheetah'
}
print(my_dict)

#modify
my_dict[2]="siberian tiger"
print(my_dict)

#add
my_dict[5]="cat"
print(my_dict)

#update(combine 2 dicts)
my_newdict={
    5:10,
    6:20,
    7:30
}
my_dict.update(my_newdict)
print(my_dict)

#delete item using key
del my_dict[3]
print(my_dict)

#delete an entire dict
# del my_dict
# print(my_dict)

#pop ( can display the deleted item)
# a=my_dict.pop(4)
# print(a)
print(my_dict.pop(4))

print(len(my_dict))
print(type(my_dict))


#printing keys only
print(my_dict.keys())

#printing values only
print(my_dict.values())

