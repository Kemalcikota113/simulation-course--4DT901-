import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Given data from the last week of production
days = np.array([1, 2, 3, 4, 5])
total_jobs = np.array([83, 93, 112, 65, 78])
type_A_jobs = np.array([53, 62, 66, 41, 55])
type_B_jobs = total_jobs - type_A_jobs  # Calculate Type B jobs

mean_total_jobs = np.mean(total_jobs)
mean_type_A_jobs = np.mean(type_A_jobs)
mean_type_B_jobs = np.mean(type_B_jobs)

lambda_total = mean_total_jobs

proportion_type_A = np.mean(type_A_jobs / total_jobs)

simulated_total_jobs = np.random.poisson(lambda_total)