import numpy as np


N = 16 #number of random points


numIn = 0
for i in range(N):
    x = np.random.rand()*2 - 1
    y = np.random.rand()*2 - 1
    r = np.sqrt(x**2+y**2)
    if r >= 0.5 and r <=1:
        numIn += 1
area = 4*numIn/N
print(area)
