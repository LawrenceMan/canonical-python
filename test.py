import numpy as np
import sys
import keyword
import operator
from datetime import datetime
import os

# print(keyword.kwlist)

a = [0, 1, 2, 3]
# b will store values which are 1 greater than the values stored in a
b = [i + 1 for i in a]
print(b)