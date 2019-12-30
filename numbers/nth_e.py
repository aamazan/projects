# Author: Armaan Amazan
# Description: Find e to the Nth digit
import math

n = int(input())

def digits(num):
    e = str(math.exp(1))
    if num == 1:
        return num
    else:
        num = e[:(num + 1)]
        return num

print(digits(n))

# TODO: implement rounding
