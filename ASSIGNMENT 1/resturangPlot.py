import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('RAW DATA/A1 TakeAway-Dataset.csv')


df['Order Date'] = pd.to_datetime(df['Order Date'])


df['Order Hour'] = df['Order Date'].dt.floor('H')


orders_per_hour = df.groupby('Order Hour').size()
avg_delivery_time_per_hour = df.groupby('Order Hour')['Delivery Time Taken (mins)'].mean()


plt.figure(figsize=(12, 6))


plt.plot(orders_per_hour.index, orders_per_hour.values, marker='o', linestyle='-', color='b', label='Orders per Hour')


plt.plot(avg_delivery_time_per_hour.index, avg_delivery_time_per_hour.values, marker='x', linestyle='-', color='r', label='Average Delivery Time (mins)')

plt.xlabel('Order Hour')
plt.ylabel('Number of Orders / Delivery Time (mins)')
plt.title('Orders per Hour and Average Delivery Time Comparison')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
