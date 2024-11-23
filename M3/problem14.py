import numpy as np

def KStest(data, cdfFunc):
    # step 1: sort the data
    sortedData = np.sort(data)

    N = len(data)

    # step 2: compute D+ and D-
    dPlus = np.max(np.arange(1, N + 1) / N - cdfFunc(sortedData))
    print('D+: ', dPlus)
    dMinus = np.max(cdfFunc(sortedData) - (np.arange(0, N) / N))
    print('D-: ', dMinus)

    # step 4: compute D
    D = np.max([dPlus, dMinus])
    print('D: ', D)
    #D = np.max(np.abs(ecdf - cdfValues))
    
    return D

def uniformCDF(x, minValues, maxValues):
    return (x - minValues) / (maxValues - minValues)


data = np.array([88.3, 40.7, 36.3, 27.3, 36.8,
                91.7, 67.3, 7.0, 45.2, 23.3,
                98.8, 90.1, 17.2, 23.7, 97.4,
                32.4, 87.8, 69.8, 62.6, 99.7,
                20.6, 73.1, 21.6, 6.0, 45.3,
                76.6, 73.2, 27.3, 87.6, 87.2])



D = KStest(data, lambda x: uniformCDF(x, np.min(data), np.max(data)))

print('\nthe kolmogorov-smirnov test statistic is: ', D)


n = len(data)
critical_value = 1.36 / np.sqrt(n)  # Approximation for alpha = 0.05
print('the critical value is: ', critical_value)

if D > critical_value:
    print("Reject the null hypothesis (The data is not uniformly distributed).")
else:
    print("Fail to reject the null hypothesis (The data is uniformly distributed).")