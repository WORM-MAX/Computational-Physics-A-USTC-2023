import random
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#生成xyz
e = [random.uniform(-1, 1) for _ in range(5000)]
f = [random.uniform(-1, 1) for _ in range(5000)]

u = [x for x, y in zip(e, f) if x**2 + y**2 < 1]
v = [y for x, y in zip(e, f) if x**2 + y**2 < 1]

r2 = [i*i+j*j for i,j in zip(u,v)]
x = [2*a*math.sqrt(1-b) for a,b in zip(u,r2)]
y = [2*a*math.sqrt(1-b) for a,b in zip(v,r2)]
z = [1-2*a for a in r2]

#画图
fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection='3d')

ax1.scatter(x, y, z, s=0.2)

ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

plt.show()

#二维投影
plt.scatter(x, y, s=0.2)
plt.show()