def greet():
    print("Hello!")

greet()


def cub(a):
    return a*a

print(cub(2))

def sum(a: int,b: int)->int:
    return a+b
print(sum(7,3))

###

# def function
def cylinder_vol(rad, h):
    return 3.14 * rad**2 * h
result = cylinder_vol(2,4)
print(result)

# lambda function 
cylinder_vol2 = lambda rad, h: 3.14 * rad**2 * h
result2 = cylinder_vol2(2,4)
print(result2)

with open('file.txt', 'r') as archivo:
    content = archivo.read()
    print(content)

with open('file2.txt', 'w') as archivo:
    archivo.write("Hola mundo")

###
numeros = [1,2,3,4,5]

def cubico(number):
    return number**3

result = map(cubico, numeros)
resultLambda = map(lambda x: x**3, numeros)

print(list(result))
print(list(resultLambda))

### 

numeros = [1,2,3,4,5,6,7,8,9]

result = filter(lambda x: x>5, numeros)

print(list(result))

###

from functools import reduce

numeros = [1,2,3,4,5,6,7,8,9]
result = reduce(lambda x,y: x+y, numeros, 4)
print(result)