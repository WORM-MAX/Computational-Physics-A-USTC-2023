import random
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#坐标生成
a = [random.uniform(0, 1) for _ in range(5000)]
b = [random.uniform(0, 1) for _ in range(5000)]

x = [math.sqrt(2*j-j*j)*math.cos(2*math.pi*i) for i,j in zip(a,b)]
y = [math.sqrt(2*j-j*j)*math.sin(2*math.pi*i) for i,j in zip(a,b)]
z = [1-j for j in b]

#画图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.scatter(x, y, z, s=0.2)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()