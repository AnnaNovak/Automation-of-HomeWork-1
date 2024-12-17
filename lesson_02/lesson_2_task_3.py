import math

def square(side):

    area = side ** 2
    return math.ceil(area)


print(square(4))      
print(square(3.5))    
print(square(2.1))  