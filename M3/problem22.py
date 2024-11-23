import numpy as np
import matplotlib.pyplot as plt


data = np.array([0,2,0,0,0,
                1,0,1,1,1,
                0,1,0,0,0,  
                2,0,1,0,1,
                0,1,0,0,2,
                1,0,1,0,0,
                0,0,0,0,0,
                1,0,1,0,1,
                0,0,3,0,1,
                1,0,0,0,0])

# H0: The data follows a Poisson distribution
# H1: The data does not follow a Poisson distribution

mean = np.mean(data)
print(mean)

# amount of times 1, 2 and 3 appears in the data
obeserved_0 = np.count_nonzero(data == 0)
print(obeserved_0)

observed_1 = np.count_nonzero(data == 1)
print(observed_1)

observed_2 = np.count_nonzero(data == 2)
print(observed_2)

observed_3 = np.count_nonzero(data == 3)
print(observed_3)

# get the expected values
expected_0 = len(data) * np.exp(-mean)
print(expected_0)

expected_1 = len(data) * mean * np.exp(-mean)
print(expected_1)

expected_2 = len(data) * (mean**2) * np.exp(-mean) / 2
print(expected_2)

expected_3 = len(data) * (mean**3) * np.exp(-mean) / 6
print(expected_3)

chisq_0 = ((obeserved_0 - expected_0)**2) / expected_0
print(chisq_0)
chisq_1 = ((observed_1 - expected_1)**2) / expected_1
print(chisq_1)
chisq_2 = ((observed_2 - expected_2)**2) / expected_2
print(chisq_2)
chisq_3 = ((observed_3 - expected_3)**2) / expected_3
print(chisq_3)

chisq = chisq_0 + chisq_1 + chisq_2 + chisq_3
print('chisq = ', chisq)