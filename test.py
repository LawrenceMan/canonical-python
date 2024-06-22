import numpy as np
import sys
import keyword
import operator
from datetime import datetime
import os

# print(keyword.kwlist)

a = {0, 1, 2, 3}
# b will store squares of the elements of a
b = {i ** 2 for i in a}
print(b)