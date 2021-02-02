# import numpy as np

# R1 = np.random([3,7])
# print(R1)
# print("\n")
# R2 = np.random([7,2])
# print(R2)
# print("\n")
# print("\n")

# R3 = R1.dot(R2) #DOT product tra matrici con egual numero di righe
# print(R3)
import numpy as np
import matplotlib.pyplot as plt

x = [0,3,2,5]
y = [0,4,0,7]

# plt.plot(x,y) #genera il grafico
# plt.show() #comando per aprire il grafico in pyluncher

# plt.plot(3*np.array(x), 4*np.array(y))
# plt.plot(10*np.random.rand(20),10*np.random.rand(20))



plt.title("test")
plt.plot(10*np.random.rand(20),10*np.random.rand(20))
plt.plot(3*np.array(x), 4*np.array(y))
plt.show() #fa vedere la figura test con il grafico dei due plot insieme 