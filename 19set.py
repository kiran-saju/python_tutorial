#unordered,heterogenous,mutable,no duplication, no indexnumber

my_set={8,4,9,'lion','tiger','tiger'}
print(my_set)
print(type(my_set))
print(len(my_set))

#add()
my_set.add("jaguar")
print(my_set)

#update - to add multiple items
my_set.update(['puma','cat','dog'])
print(my_set)

#remove-delete specific items
my_set.remove("lion")
print(my_set)

#clear
my_set.clear()
print(my_set)

#delete
'''del my_set
 print(my_set)
 '''