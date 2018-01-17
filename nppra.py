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
print(np.random.random((3,3,3))


#13
a = np.random.random((3,3,3))
minn = a.min()
maxx = a.max()
print(minn,maxx)

#14
a = np.random.random(30)
print(a.mean())

#15 see ans
Z = np.ones((10,10))
Z[1:-1,1:-1] = 0
print(Z)

#16 see ans pad == padding
Z = np.ones((5,5))
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
print(Z)

#17 see ans  diag==対角成分の取得
Z = np.diag(1+np.arange(4),k=-1)
print(Z)

#18
Z = np.zeros((8,8),dtype=int)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)
