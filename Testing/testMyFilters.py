import os
import sys


sys.path.append(os.path.join(os.getcwd(), '../lib'))

from vtk import *
from vtkMyFiltersPython import *

f = vtkMyFilter()
print f
