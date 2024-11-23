import numpy as np
import matplotlib.pyplot as plt

# Given average call rates per hour (lambda values)
average_calls_per_hour = [25.2, 39, 59.2, 79.8, 70.6, 40.6, 43.2, 19.4]

def nspp(lambdas, hours):
    call_times = []
    calls_per_hour = [] 
    current_time = 0

    for i, rate in enumerate(lambdas):
        # Number of calls in the hour, drawn from a Poisson distribution
        num_calls = np.random.poisson(rate)
        calls_per_hour.append(num_calls)
        
        # Generate interarrival times for the calls
        if num_calls > 0:
            interarrival_times = np.random.exponential(1 / rate, num_calls)
            arrival_times = current_time + np.cumsum(interarrival_times)
            call_times.extend(arrival_times)
        
        # Move the time forward by 1 hour (to the next interval)
        current_time += 1
    
    return np.array(call_times), calls_per_hour


hours = np.arange(8, 17)  # Hour ranges from 8 to 16 (representing 8 A.M. to 4 P.M.)
call_times, calls_per_hour = nspp(average_calls_per_hour, hours)

# Step 3: Plot the simulated call arrivals
plt.figure(figsize=(10, 6))
plt.hist(call_times, bins=9, edgecolor='black', alpha=0.7)
plt.title('Simulated Call Arrivals (NSPP Model)')
plt.xlabel('Time of Day (in hours)')
plt.ylabel('Number of Calls')
plt.grid(True)
plt.show()

# Display the average call rates per hour (lambda values)
print("Average call rates (lambda values) per hour from 8 A.M. to 4 P.M.:")
for i, rate in enumerate(average_calls_per_hour):
    print(f"{hours[i]}–{hours[i]+1} P.M.: λ = {rate:.2f} calls/hour")

print("\n\nSimulated number of calls per hour from 8 A.M. to 4 P.M.:")
for i, num_calls in enumerate(calls_per_hour):
    print(f"{hours[i]}–{hours[i]+1} P.M.: {num_calls} calls")

