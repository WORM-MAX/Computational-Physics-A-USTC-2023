#16807 random number generator
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