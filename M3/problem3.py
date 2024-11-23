import numpy as np
import matplotlib.pyplot as plt

# Parameters
n_vehicles = 500  # Total number of vehicles for the simulation
peak_interarrival = 20  # Peak hour mean interarrival time (seconds)
offpeak_interarrival = 45  # Off-peak hour mean interarrival time (seconds)

# Simulate traffic for morning rush, midday, and evening rush
def generate_interarrival_times(n_vehicles, mean_interarrival):
    return np.random.exponential(scale=mean_interarrival, size=n_vehicles)

# Define different traffic periods
morning_rush = generate_interarrival_times(n_vehicles//3, peak_interarrival)
midday = generate_interarrival_times(n_vehicles//3, offpeak_interarrival)
evening_rush = generate_interarrival_times(n_vehicles//3, peak_interarrival)

# Concatenate to get the full day's traffic data
all_interarrival_times = np.concatenate((morning_rush, midday, evening_rush))

# Cumulative arrival times (in seconds)
arrival_times = np.cumsum(all_interarrival_times)

# Vehicle direction behavior (60% straight, 25% right, 15% left)
turn_probabilities = [0.60, 0.25, 0.15]  # [Straight, Right, Left]
turns = np.random.choice(['Straight', 'Right', 'Left'], size=n_vehicles, p=turn_probabilities)

# Simulate accidents (happens randomly every ~200 cars, no cars arrive for 10 minutes)
accident_prob = 1 / 200  # Probability of an accident occurring
accident_times = []
for i in range(n_vehicles):
    if np.random.rand() < accident_prob:
        accident_times.append(arrival_times[i] + np.random.uniform(600, 700))  # Accident lasts for 10 mins

# Print sample data
print(f"Sample arrival times (first 10): {arrival_times[:10]}")
print(f"Sample vehicle behavior (first 10): {turns[:10]}")
if accident_times:
    print(f"Accident times: {accident_times[:5]}")

# Plot the interarrival times during the day
plt.figure(figsize=(12, 6))

plt.hist(morning_rush, bins=30, alpha=0.7, label='Morning Rush')
plt.hist(midday, bins=30, alpha=0.7, label='Midday')
plt.hist(evening_rush, bins=30, alpha=0.7, label='Evening Rush')
plt.title('Interarrival Times at an Intersection by Period')
plt.xlabel('Interarrival Time (seconds)')
plt.ylabel('Frequency')
plt.legend()
plt.show()

# Plot a timeline of vehicle arrivals and accidents
plt.figure(figsize=(12, 6))
plt.plot(arrival_times, np.arange(n_vehicles), label='Vehicle Arrivals')
for accident in accident_times:
    plt.axvline(accident, color='red', linestyle='dashed', label='Accident')
plt.title('Cumulative Vehicle Arrivals and Accidents')
plt.xlabel('Time (seconds)')
plt.ylabel('Cumulative Vehicles')
plt.legend()
plt.show()
