import numpy as np
import sys
import keyword
import operator
from datetime import datetime
import os

# print(keyword.kwlist)

import logging
# Create and configues the logger
logging.basicConfig(filename="newfile.log", format='%(asctime)s %(message)s', filemode='w')
# Creates logging object
logg = logging.getLogger()
# Sets the level of logging to DEBUG
logg.setLevel(logging.DEBUG)
# Messages
logg.debug("Debug Message")
logg.warning("Its a Warning")
logg.info("Just an information")