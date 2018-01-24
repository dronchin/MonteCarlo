import numpy as np
import matplotlib.pyplot as plt

#N = 10000 number of random points
#N_list = [1,2,3,4,5,6,7,8,9,10,20,30,40,100,1000]#100,1000,10000,100000]

N_list = np.arange(1,100)

error = []

actual = np.pi - np.pi*0.25

for N in N_list:
    E_list = []
    for a in range(10): #this loop smooths out the random variations
        numIn = 0
        for i in range(N):
            x = np.random.rand()*2 - 1
            y = np.random.rand()*2 - 1
            r = np.sqrt(x**2+y**2)
            if r >= 0.5 and r <=1:
                numIn += 1
        area = 4*numIn/N
        E = np.abs(area - actual)/actual
        E_list.append(E)
    Eavg = np.average(E_list)
    error.append(Eavg)

plt.plot(N_list, error)
plt.show()
