# We use PIP (Pip Installs Packages), the official Python package manager.
# It's used to install and manage libraries and packages that aren't included in the standard library.

# Console $ pip install numpy

import numpy 

print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))
print(numpy_array*2)
