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



data = np.array([0.44, 0.53, 2.04, 2.74, 2.00, 0.30, 2.54, 0.52, 2.02, 1.89, 1.53, 0.21,
                2.80, 0.04, 1.35, 8.32, 2.34, 1.95, 0.10, 1.42, 0.46, 0.07, 1.09, 0.76,
                5.55, 3.93, 1.07, 2.26, 2.88, 0.67, 1.12, 0.26, 4.57, 5.37, 0.12, 3.19,
                1.63, 1.46, 1.08, 2.06, 0.85, 0.83, 2.44, 1.02, 2.24, 2.11, 3.15, 2.90,
                6.58, 0.64])
                

D = KStest(data, lambda x: uniformCDF(x, np.min(data), np.max(data)))

print('\nthe kolmogorov-smirnov test statistic is: ', D)


n = len(data)
critical_value = 1.36 / np.sqrt(n)  # Approximation for alpha = 0.05
print('the critical value is: ', critical_value)

if D > critical_value:
    print("Reject the null hypothesis (The data is not uniformly distributed).")
else:
    print("Fail to reject the null hypothesis (The data is uniformly distributed).")