import numpy as np
import sys
import keyword
import operator
from datetime import datetime
import os

# print(keyword.kwlist)

# a=sys.path()  # Error


def sub_decorator(func):
    def wrapper(num1,num2):
        if num1 < num2:
            num1, num2 = num2, num1
        return func(num1,num2)
    return wrapper

print('w/o using @:')
def subtract(num1, num2):
    res = num1 - num2
    print('Result is :- ',res)

sub=sub_decorator(subtract)
sub(2,4)

print('using @:')
@sub_decorator # we can use @ syntax for decorating a function in one step
def subtract(num1, num2):
    res = num1 - num2
    print('Result is :- ',res)

subtract(2,4)
