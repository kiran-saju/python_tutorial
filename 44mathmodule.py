import math
#ceil
#without ceil
a=8/3
print(a)
#using ceil
print(math.ceil(a))


#floor
#without floor
a=8/3
print(a)
#using ceil
print(math.floor(a))


#pow()
#without pow()
a=2**3
print(a)
#with pow()
print(math.pow(2,3)) #out put will be in floor value

#without import pow()
a=pow(2,3)
print(a) #out put will not be in floor value

a=pow(2,4,5)
print(a)
#out put will be 1, becz (2**4)%5

#fabs() - absolute
print(math.fabs(-5)) #out put will be in floor value
#without importing fabs()  we use abs()
print(abs(-5)) #out put will not be in floor value

#degrees() - getting degree from radian
print(math.degrees(100))

#radians() - getting radian from degree 
print(math.radians(5729.5779513082325))

#pi
print(math.pi)

#e
print(math.e)

#find all functions of math module
help(math)

