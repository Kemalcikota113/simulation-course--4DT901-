import pandas as pd
from datetime import datetime

# Read the CSV file
df = pd.read_csv('RAW DATA/A1 TakeAway-Dataset.csv')

# Convert 'Order Date' column to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Calculate the time differences between each order (arrival times)
df = df.sort_values('Order Date')
df['Time Difference (mins)'] = df['Order Date'].diff().dt.total_seconds() / 60.0

# Calculate arrival rate
average_time_between_arrivals = df['Time Difference (mins)'].mean()
arrival_rate = 1 / average_time_between_arrivals  # λ = 1 / average inter-arrival time

# Calculate service rate 
average_service_time = df['Delivery Time Taken (mins)'].mean()
service_rate = 1 / average_service_time  # μ = 1 / average service time

# main
print(f"Arrival rate (λ): {arrival_rate:.4f} customers per minute")
print(f"Service rate (μ): {service_rate:.4f} customers per minute")


print(f"Average time between arrivals: {average_time_between_arrivals:.4f} minutes")
print(f"Average service time: {average_service_time:.4f} minutes")


df['Time Difference (mins)'].hist(bins=20, alpha=0.7)
df['Delivery Time Taken (mins)'].hist(bins=20, alpha=0.7)
