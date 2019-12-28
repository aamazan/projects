# Author: Armaan Amazan
# Description: Find pi to the Nth digit
import math

n = int(input())

def digits(num):
    p = str(math.pi)
    if num == 1:
        return num
    else:
        num = p[:(num + 1)]
        return num

print(digits(n))

# TODO: implement rounding
