#list

#heterogenous
 
a=[1,2,3,"tiger","lion"]
#  0 1 2  3       4
print(type(a),a)
print(a)

#ordered 
print(a.index("tiger")) #3
print(a.index(1)) #0

#slicing in list
print(a[3]) #tiger
print(a[0:4]) # 0,1,2,3,tiger
print(a[-1:-4:-1]) #lion,tiger,3

#mutable
a[3]="Jaguar"
print(a) #[1, 2, 3, 'Jaguar', 'lion']
print(len(a))

b=[9,2,7,1,4,5]
print(b)

#sorting
b.sort()
print(b)

#descending order
b.sort(reverse=True)
print(b)

#reverse
c=[9,2,7,1,4,5]
print(c)
c.reverse()
print(c)

#max()
print(max(c))

#min()
print(min(c))

#append() - add new item to last place of an list
c.append(25)
print(c)

#insert() - insert to an index positions
c.insert(1,12) # 1 is index pos and 12 is the value to be inserted
print(c)

#extend() - add multiple items to back of a list
c.extend([50,100,500,500])
print(c)

#remove() - remove specific item 
c.remove(500) #first 500 removed
print(c) #only first occured item is removed if same item name exsists

#pop()-remove last item
c.pop()
print(c) #500 removed

c.pop(3) #index pos 3 is removed
print(c)

#count()- count of multiple items with same name
c.extend([5,5,5,5])
print(c)
print(c.count(5))

#clear() - clearing items
c.clear()
print(c)


#nested list
my_list=[1,2,3,["lion","tiger","zebra"],4,5]
#        0 1 2        3                 4  5
#                 0        1      2


#(list_index_no,item_index_no)
print(my_list[3][0]) #lion
print(my_list[3][1]) #tiger
print(my_list[3][2]) #zebra

#index_positions
print(my_list.index(1))
print(my_list.index(2))
print(my_list[3].index("tiger"))
d=my_list[3]
print(d.index("lion"))
print(my_list.index(4))
print(my_list.index(5))

del my_list
# print(my_list)