import numpy as np
import matplotlib.pyplot as plt

# Simulating interarrival times (Exponential distribution with mean 5 minutes)
n_customers = 100  # Let's assume we are simulating 100 customers
interarrival_times = np.random.exponential(scale=5, size=n_customers)

# Simulating service times for two workers (normal distributions)
service_times_worker1 = np.random.normal(loc=4, scale=1, size=n_customers // 2)
service_times_worker2 = np.random.normal(loc=6, scale=2, size=n_customers // 2)

# Combine service times from both workers
service_times = np.concatenate((service_times_worker1, service_times_worker2))

# Simulating service times for two types of appliances (triangular distribution)
service_times_typeA = np.random.triangular(left=3, mode=5, right=10, size=n_customers // 2)
service_times_typeB = np.random.triangular(left=4, mode=8, right=12, size=n_customers // 2)

# Combine service times from both types
service_times_appliance = np.concatenate((service_times_typeA, service_times_typeB))

# Print a sample of the interarrival and service times
print(f"Interarrival times (first 10): {interarrival_times[:10]}")
print(f"Service times for Worker 1 (first 10): {service_times_worker1[:10]}")
print(f"Service times for Worker 2 (first 10): {service_times_worker2[:10]}")
print(f"Service times for Type A appliance (first 10): {service_times_typeA[:10]}")
print(f"Service times for Type B appliance (first 10): {service_times_typeB[:10]}")

# Plotting the distributions

# Interarrival times distribution
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(interarrival_times, bins=30, edgecolor='black', density=True)
plt.title('Histogram of Interarrival Times')
plt.xlabel('Interarrival Time (minutes)')
plt.ylabel('Density')

# Service times distribution (workers)
plt.subplot(1, 2, 2)
plt.hist(service_times_worker1, bins=30, alpha=0.5, label='Worker 1', density=True)
plt.hist(service_times_worker2, bins=30, alpha=0.5, label='Worker 2', density=True)
plt.title('Histogram of Service Times by Worker')
plt.xlabel('Service Time (minutes)')
plt.ylabel('Density')
plt.legend()

plt.tight_layout()
plt.show()

# Plotting the service times by appliance type
plt.figure(figsize=(6, 6))
plt.hist(service_times_typeA, bins=30, alpha=0.5, label='Appliance Type A', density=True)
plt.hist(service_times_typeB, bins=30, alpha=0.5, label='Appliance Type B', density=True)
plt.title('Histogram of Service Times by Appliance Type')
plt.xlabel('Service Time (minutes)')
plt.ylabel('Density')
plt.legend()
plt.show()
