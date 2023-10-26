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

# Get current time
current_time = datetime.now()
year = current_time.year
month = current_time.month
day = current_time.day
hour = current_time.hour
minute = current_time.minute
second = current_time.second

#Function for random number generation
def generate(N = int(1e8)):
    I = np.zeros(N)
    X = np.zeros(N, dtype=float)

    #seed
    I[0]=year + 70*(month + 12*(day + 31*(hour + 23*(minute + 59*second))))
    X[0] = I[0]/m

    for n in range(N-1):
        I[n+1] = a*(I[n]%q)-r*int(I[n]/q)
        if I[n+1] <= 0:
            I[n+1] += m
        X[n+1] = I[n+1]/m
    
    return X

#X is a random number list and used in the whole expriment
# Default length is 1e8
X = generate()

#Plot: pairs of data points with interval of 3
l = 3
x = X[0:2500]
y = X[l:2500+l]  # y轴数据

plt.figure(dpi=300)
plt.scatter(x, y, color='blue', s=0.2)
plt.title('l=3')
plt.xlabel(r'$X_{n}$')
plt.ylabel(r'$X_{n+3}$')
plt.rc('text', usetex=True)
plt.show()

#xk
n = range(10,int(1e8))
for k in [3,4,5,6]:
    p = range(1,9)
    N = np.power(10, p)
    error = np.zeros((4,len(p)), dtype=float)
    for i in range(len(N)):
        error[k-3][i] = abs(np.power(X[:N[i]], k).mean() - 1/(1+k))

    plt.semilogx()
    plt.plot(N, error[k-3], '-o', label='error')
    plt.plot(n, error[k-3][0]*np.sqrt(10)*np.reciprocal(np.sqrt(n)), '--', label=r'$\frac{1}{\sqrt{N}}$')
    plt.title(str(k)+'th moment with size N')
    plt.xlabel('N')
    plt.ylabel('error')
    plt.rc('text', usetex=True)
    plt.show()


#C(l)
L = range(2,10)

def variance(X, l):
    a = X[:-l]
    b = X[l:]
    return ((a*b).mean()-(X.mean())**2)/np.var(X)
for l in L:
    c = variance(X, l)
    print("l = {}, C(l) = {}".format(l,c))