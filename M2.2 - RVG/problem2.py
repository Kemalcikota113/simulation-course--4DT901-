import numpy as np
import pandas as pd

# Firsts we need to define the uniform distribution

a = 2   # min
b = 6 # max
c = 3 # mode --> the function changes at this point

def randomVar():
    U = np.random.rand()

    if U < 0.25:
        x = 2 + 2*np.sqrt(U)

    else:
        x = 6 - 2 * np.sqrt(3 - 3*U)
    
    return x

# generate random variables

n = 1000 # number of random variables
#randomVars = [randomVar() for i in range(n)]

n = 1000  # number of random variables
randomVars = [randomVar() for i in range(n)]

randomVarsMean = np.mean(randomVars)

print('This is the sample mean: ', randomVarsMean)

true_mean = (a + b + c) / 2
print("This is the true mean: ", true_mean)

