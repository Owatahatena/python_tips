#1
import numpy as np

#2
print(np.__version__)
print(np.__config__.show())

#3
a = np.zeros(10)
a[:] = np.nan
print(a)

#4
import sys
print(sys.getsizeof(a))

#5
#???


#6
a = np.zeros(10)
a[4] = 1
print(a)

#7
a = np.arange(10,50)
print(a)

#8
print(a[::-1])

#9
a = np.arange(8)
print(a.reshape(3,3))


#10
l = [1,2,0,0,4,0]
print(np.nonzero(l))


#11
a = np.eye(3)
print(a)

#12
print(random.random((3,3,3))
