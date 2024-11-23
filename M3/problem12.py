import numpy as np

data = [1.691, 1.437, 8.221, 5.976, 1.116, 4.435, 2.345, 1.782, 3.810, 4.589, 5.313, 10.90, 2.649, 2.432, 1.581, 2.432, 1.843, 2.466, 2.833, 2.361]

#sample mean:
sample_mean = np.mean(data)
print('sample mean: ', sample_mean)

#sample variance:
sample_variance = np.var(data)
print('sample variance: ', sample_variance)

lnX = np.log(data)
lnX_sum = np.sum(lnX)
lnX_mean = np.mean(lnX)
print('lnX_sum: ', lnX_sum)

alpha_hat = (sample_mean**2) / (sample_variance**2)
beta_hat = (sample_variance**2) / (sample_mean**2)

print('\nestimation of alpha-hat: alpha-hat ≈ ', alpha_hat)
print('estimation of beta-hat: beta-hat = ', beta_hat)