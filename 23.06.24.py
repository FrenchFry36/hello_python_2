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

# labda function 
cylinder_vol2 = lambda rad, h: 3.14 * rad**2 * h
result2 = cylinder_vol2(2,4)
print(result2)

with open('file.txt', 'r') as archivo:
    content = archivo.read()
    print(content)

with open('file2.txt', 'w') as archivo:
    archivo.write("Hola mundo")
