import numpy as np
import matplotlib.pyplot as plt

data = np.array([0.661, 4.910, 8.989, 12.801, 20.249,
        5.124, 15.033, 58.091, 1.543, 3.624,    
        13.509, 5.745, 0.651, 0.965, 62.146,
        15.512, 2.758, 17.602, 6.675, 11.209,
        2.731, 6.892, 16.713, 5.692, 6.636,
        2.420, 2.984, 10.613, 3.827, 10.244,
        6.255, 27.969, 12.107, 4.636, 7.093,
        6.892, 13.243, 12.711, 3.411, 7.897,
        12.413, 2.169, 0.921, 1.900, 0.315,
        4.370, 0.377, 9.063, 1.875, 0.790])

# H0: The data follows a exponential distribution
# H1: The data does not follow a exponential distribution

lambda_est = 1 / np.mean(data)
print(lambda_est)



