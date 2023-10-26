from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

a = 16807
m = 2147483647
#m=a*127773+2836
q= 127773
r = 2836
#I_n+1 = a*I_n mod(m)
#x_n = I_n/m

#Function of 16807 for random number generation
def generate1(current_time, N = int(1e8)):
    year = current_time.year
    month = current_time.month
    day = current_time.day
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second

    I = np.zeros(N ,dtype='int32')

    #seed
    I[0]=year + 70*(month + 12*(day + 31*(hour + 23*(minute + 59*second))))

    for n in range(N-1):
        I[n+1] = a*(I[n]%q)-r*int(I[n]/q)
        if I[n+1] <= 0:
            I[n+1] += m
    
    return I

#X is a random number list and used in the whole expriment
# Default length is 1e8
#    X = np.zeros(N, dtype=float)

#Function of Fibonacci for random number generation
def generate2(I0, N = int(1e8)):
    I = np.zeros(N, dtype='int32')
    I[:43] = I0[:43]
    
    for n in range(43, N):
        I[n] = I[n-22] - I[n-43]
        if I[n]<=0:
            I[n] += 2^32-5-1
    
    return I



#计算比重
def count(I):
    count = 0
    for i in range(len(I)-2):
        if I[i]>I[i+2] and I[i+2]>I[i+1]:
            count += 1
    return count/(len(I)-2)

count1 = np.zeros(5, dtype='float')
count2 = np.zeros(5, dtype='float')

for i in range(5):
    # Get current time for seed
    current_time = datetime.now()
    I1 = generate1(current_time)
    count1[i] = count(I1)
    I2 = generate2(I1)
    count2[i] = count(I2)

print("5个16807产生的随机序列中Xn-1>Xn+1>Xn的比重分别为\n")
for i in range(5):
    print('{:.7f}\n'.format(count1[i]))
print("平均值为{:.7f} 与理想值差为{:.7f}\n".format(count1.mean(), abs(1/6-count1.mean())))
print("5个Fibonacci延迟产⽣器产生的随机序列中Xn-1>Xn+1>Xn的比重\n")
for i in range(5):
    print('{:.7f}\n'.format(count2[i]))
print("平均值为{:.7f} 与理想值差为{:.7f}\n".format(count2.mean(), abs(1/6-count2.mean())))