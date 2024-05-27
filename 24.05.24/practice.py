array1 = [True,  True,  True,  False,
                  True,  True,  True,  True ,
                  True,  False, True,  False,
                  True,  False, False, True ,
                  True,  True,  True,  True ,
                  False, False, True,  True ]

def count_sheeps(array1):
    x = 0
    for el in array1:
        if el:
            x = x + 1
    return x

result = count_sheeps(array1)
# print(result)
