'''def topten():
    yield 5  

values = topten()  

print(values)





def topten():

   yield 5



values = topten()


print(values.__next__())


def mygen():
    n=1
    yield n
    print('first')
me = mygen()
print(me.__next__())



def rev(boy):
    len1=len(boy)
    for i in range (len1-1,-1,-1):
      yield boy[i]



for c in rev("he is one of the mistorious"):
      print(c)



def divide_numbers(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b  

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))

result = divide_numbers(a, b)  
print("Result of", a, "/", b, "is:", result)


a=5
b=6
print(sum is a/b)


a=5
b=2
try:
    print(a/b)
    k=int(input('enter a number'))
    print(k)
except ZeroDivisionError:
    print("you cant do this ")
except ValueError :
    print("invlid error")
except exception :
    print("something went wrong...")

finally:
    print("file is closed")'''






import re
pattern = re.compile("python")
result = pattern.findall("welcome to python progmming. python is object oriented.")
print(result)
result2 = pattern.findall("learning python is simple")
print(result2)
































