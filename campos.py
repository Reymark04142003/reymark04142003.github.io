def my_function(fname):
    print(fname)

my_function("Emil")

def my_function(*kids):
    print("The younges child is" + kids[2])

my_function("Emil","Tobias","Linus")

def my_function(country= "norway"):
    print("i am from" + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(food): 
    for x in food:
        print(x)

fruits= ["apple", "banana","cherry"]
my_function(fruits)

def my_function(x):
    return 5* x

print(my_function(3))
print(my_function(5))
print(my_function(9))

def myfunction():
    pass

def my_function(x, /):
    print(x)

def my_function(x):
    print(x)

my_function(x=3) 

def my_function(a,b,c,d):
    print(a+b+c+d)

myfunction(5,6, c=7,d=8)