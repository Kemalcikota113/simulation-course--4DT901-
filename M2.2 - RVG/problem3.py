import numpy as np

# parameters for the triangular distribution

def customRandomVar(a, b, c):

    U = np.random.rand()

    if U < ((b - a) / (c - a)):
        return a + np.sqrt((b - a) * (c - a) * U)
    else:
        return c - np.sqrt((c - a) * (c - b) * (1 - U))


a = 1  # min
b = 10  # max
c = 4  # mode --> The function changes at this point

randomVars = []     # array to store values

for i in range(1000):

    RandomVar = customRandomVar(a, b, c)
    randomVars.append(RandomVar)

randomVarsMean = np.mean(randomVars)
distributionMean = (a + b + c) / 3

print('This is the sample mean: ', randomVarsMean)
print('This is the mean of the distribution: ', distributionMean)

meanDiff = randomVarsMean - distributionMean

print('difference between the means: ', meanDiff)



    



