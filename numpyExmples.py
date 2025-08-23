import numpy as np

numberList = [1,2,3,4,5,6]

updatedNumber = [number * 3 if number %2 == 0 else number * 2 for number in numberList]
print(updatedNumber)