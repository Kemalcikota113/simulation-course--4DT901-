import sys

import math
import random

class QueueSimulation:
	# CONSTANT VARS
	ARR, DEP, EXT = 0, 1, 3  # Constants for arrival, departure, and exit events

	def __init__(self, active_hours=24*60, active_days=10, bufferSize=6, available_servers=4, serviceRate=10.499, arrivalRate=34):
		# SIMULATION CONFIG CONSTANTS
		self.active_hours = active_hours 											# simulation time for each day
		self.active_days = active_days 												# number of days to run the sim
		self.queue_max = bufferSize													# maximum number of customers allowed at once in the queue
		self.available_servers = available_servers									# number of available servers in the system
		
		# SERVICE/ARRIVAL(rate) PARAMS
		self.customer_mean_service_time = serviceRate
		self.arrival_interval = arrivalRate

		# EVENT/CUSTOMER COUNTERS
		self.accounted = 0 															
		self.delayed = 0 														
		self.queued_event = 0 													

		# CLOCK & TIME/STATISTICAL VARS
		self.clock = 0.0														
		self.prev_time = 0.0											
		self.customer_system_timer = 0.0											
		self.delay_count = 0.0													
		self.completed_delayed = 0												
		self.declined = 0														

		# Queue and server utilization trackers
		self.queue_curve_area = 0.0												
		self.server_uptime = 0.0													

		# CUSTOMER_QUEUE and SERVER STATES
		self.customer_queue = []													
		self.customer_ETA = 0.0														
		self.ready_servers = []														

	# HELPER FUNCTION TO RESET SIMULATION STATE
	def reset(self):
		self.ready_servers = []
		self.clock = 0.0
		self.customer_queue = []

	# FUNCTION TO INITIALIZE THE INITIAL STATE OF THE SIMULATION
	def initialize(self):
		self.server_uptime = 0.0
		self.customer_ETA = self.clock + self.next_event_time(self.arrival_interval)
		self.declined = 0
		self.delayed = 0
		self.accounted = 0
		self.customer_system_timer = 0.0
		self.queue_curve_area = 0.0

	def timing(self, days_count):
		earliest_event = min([self.customer_ETA, self.active_hours * days_count] + self.ready_servers)

		if earliest_event == self.customer_ETA:
			self.queued_event = self.ARR
		elif earliest_event == days_count * self.active_hours:
			self.queued_event = self.EXT
		elif earliest_event in self.ready_servers:
			self.queued_event = self.DEP
		else:
			print("missing event")
			sys.exit(1)

		self.clock = earliest_event

	# FUNCTION TO HANDLE CUSTOMER ARRIVALS
	def arrival(self):
		self.accounted += 1
		self.customer_ETA = self.clock + self.next_event_time(self.arrival_interval)
		if len(self.ready_servers) == self.available_servers:
			if len(self.customer_queue) <= self.queue_max:
				self.customer_queue.append(self.clock)
				self.customer_queue.sort()
			else:
				self.declined += 1
		else:
			self.delayed += 1
			service_time = self.next_event_time(self.customer_mean_service_time)
			self.customer_system_timer += service_time
			self.ready_servers.append(self.clock + service_time)
			self.ready_servers.sort()

	# FUNCTION TO HANDLE CUSTOMER DEPARTURES
	def depart(self):
		self.ready_servers.pop(0)
		if len(self.customer_queue) > 0:
			delay = self.clock - self.customer_queue.pop(0)
			self.delay_count += delay
			self.delayed += 1
			service_time = self.next_event_time(self.customer_mean_service_time)
			self.ready_servers.append(self.clock + service_time)
			self.ready_servers.sort()
			self.customer_system_timer += (delay + service_time)

	# FUNCTION TO UPDATE TIME-AVERAGED STATISTICS
	def refresh_statistics(self):
		time_since_last_event = self.clock - self.prev_time
		self.prev_time = self.clock
		self.queue_curve_area += len(self.customer_queue) * time_since_last_event
		self.server_uptime += (len(self.ready_servers) / self.available_servers) * time_since_last_event

	# FUNCTION TO GENERATE EXPONENTIALLY DISTRIBUTED TIME FOR EVENTS
	@staticmethod		# we can do this or send in the self parameter in the function (self, rate)
	def next_event_time(rate):
		return -math.log(random.random()) / rate    # calculate and return the next event time based on exponential dist with the given rate

	# FUNCTION TO CALCULATE MEAN AND VARIANCE
	def getMV(nums):
		mean = sum(nums) / len(nums)
		return mean, sum((x - mean) ** 2 for x in nums) / (len(nums) - 1)   # get the mean and variance

	# MAIN FUNCTION TO RUN THE SIMULATION FOR ALL DAYS
	def run_simulation(self):
		days_count = 1
		runs_data = []

		while days_count <= self.active_days:
			self.initialize()
			while True:
				self.timing(days_count)
				self.refresh_statistics()
				if self.queued_event == self.ARR:
					self.arrival()
				elif self.queued_event == self.DEP:
					self.depart()
				elif self.queued_event == self.EXT:
					break
			internal_clock = self.clock - (days_count - 1) * self.active_hours
			runs_data.append({
				'customers served': self.delayed,
				'total arrivals': self.accounted,
				'total queue': self.queue_curve_area,
				'area_server_status': self.server_uptime,
				'dropped customers': self.declined,
				'clock (min)': internal_clock,
				'total spent in system': self.customer_system_timer,
				'response time (min)': self.customer_system_timer / self.delayed if self.delayed > 0 else 0,
				'server utilization': (self.server_uptime / internal_clock) if internal_clock > 0 else 0,
				'drop rate (min^-1)': self.declined / internal_clock if internal_clock > 0 else 0,
				'drop rate (%)': (self.declined / self.accounted) * 100 if self.accounted > 0 else 0,
			})
			days_count += 1

		return runs_data

# INITIALIZE SIMULATION AND PRINT RESULTS
simulation = QueueSimulation()
runs_data = simulation.run_simulation()

# PRINT STATISTICS AND HEADERS
headers = ['customers served', 'total arrivals', 'total queue', 'dropped customers', 'clock (min)', 'response time (min)', 'server utilization', 'drop rate (min^-1)', 'drop rate (%)']
header_row = " | ".join(f"{header:<20}" for header in headers)
print(header_row)
print("-" * len(header_row))  # Print a separator line

for entry in runs_data:
    row = " | ".join(f"{entry[key]:<20}" for key in headers)
    print(row)

# AVERAGE AND VARIANCE CALCULATIONS
avg_response_time, variance_response_time = QueueSimulation.getMV([run['response time (min)'] for run in runs_data])
avg_server_utilization, variance_server_utilization = QueueSimulation.getMV([run['server utilization'] for run in runs_data])
avg_drop_rate, variance_drop_rate = QueueSimulation.getMV([run['drop rate (min^-1)'] for run in runs_data])

# PRINT FINAL STATISTICS
print("\nAverage response time:", avg_response_time)
print("Average server utilization:", avg_server_utilization)
print("Average drop rate:", avg_drop_rate)
print("\nVariance response time:", variance_response_time)
print("Variance server utilization:", variance_server_utilization)
print("Variance drop rate:", variance_drop_rate)

# CONFIDENCE INTERVAL CALCULATIONS
conf_interval_response_time = 2.26 * math.sqrt(variance_response_time / len(runs_data))
conf_server_utilization = 2.26 * math.sqrt(variance_server_utilization / len(runs_data))
conf_drop_rate = 2.26 * math.sqrt(variance_drop_rate / len(runs_data))

print("\nConfidence interval response time:", avg_response_time, "±", conf_interval_response_time)
print("Confidence interval server utilization:", avg_server_utilization, "±", conf_server_utilization)
print("Confidence interval drop rate:", avg_drop_rate, "±", conf_drop_rate)

# REPETITIONS NEEDED FOR 95% CONFIDENCE WITH 10% MARGIN OF ERROR
margin_of_error = 0.1  # desired margin of error
repetitions_for_response_time = (1.96 * math.sqrt(variance_response_time) / margin_of_error) ** 2
repetitions_for_server_utilization = (1.96 * math.sqrt(variance_server_utilization) / margin_of_error) ** 2
repetitions_for_drop_rate = (1.96 * math.sqrt(variance_drop_rate) / margin_of_error) ** 2

print("\nRepetitions needed for response time:", repetitions_for_response_time)
print("Repetitions needed for server utilization:", repetitions_for_server_utilization)
print("Repetitions needed for drop rate:", repetitions_for_drop_rate)