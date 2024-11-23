import pandas as pd

# Read the original CSV file with the full dataset
df = pd.read_csv('RAW DATA/A1 TakeAway-Dataset.csv')


average_service_time = df['Delivery Time Taken (mins)'].mean()

# Calculate the service rate 
service_rate = 1 / average_service_time

# main
print(f"Average service time: {average_service_time:.2f} minutes")
print(f"Service rate (μ): {service_rate:.4f} customers per minute")
