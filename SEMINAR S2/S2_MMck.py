import sys
import math
import random

clock = 0.0
ws1_buffer = [] # has 4 items only => 0tn is always being processed
ws2_buffer =[] # has 4 items only
MAX_BUFFER_SIZE = 4

future_arrival_time = 0.0
next_event = ""

mean_interarrival = 7
mean_service = 8

ws1_departure_time = 0.0
ws2_departure_time = 0.0

area_server_status = 0.0
area_server_status_s1 = 0.0
area_server_status_s2 = 0.0
time_last_event = 0.0


SEVER_STATUS_IDLE = 0
SERVER_STATUS_BUSY = 1

server_status = []

# seed_value = 43
# random.seed(seed_value)

def get_next_moment(rate):
  return -rate * math.log(random.random())

def initialize():
  global ws1_departure_time, ws2_departure_time, server_status, SEVER_STATUS_IDLE, future_arrival_time
  ws1_departure_time = sys.float_info.max
  ws2_departure_time = sys.float_info.max

  # set server status as idle
  server_status.append(SEVER_STATUS_IDLE)
  server_status.append(SEVER_STATUS_IDLE)

  # set future arrival
  future_arrival_time = clock + math.exp(mean_interarrival)
  return

# find the earlisie of arrival or departure and set next_event accordingly
def timing():
  global clock, ws1_buffer, ws2_buffer, next_event, future_arrival_time, ws1_departure_time, ws2_departure_time
  earliest_event = min([future_arrival_time, ws1_departure_time, ws2_departure_time])
  if earliest_event == future_arrival_time:
    next_event = "ARRIVAL"
  else:
    next_event = "DEPARTURE"

  clock = earliest_event

def arrival():
  global clock, future_arrival_time, ws1_buffer, ws2_buffer, ws1_departure_time, ws2_departure_time, server_status, MAX_BUFFER_SIZE
  future_arrival_time = clock + get_next_moment(mean_interarrival)


  if len(ws1_buffer) < MAX_BUFFER_SIZE:
    if len(ws1_buffer) == 0:
      server_status[0] = SERVER_STATUS_BUSY
      ws1_departure_time = clock + get_next_moment(mean_service)
    ws1_buffer.append(clock)
    #print(f"====== Arrival happened in server 1, now buffer length for server 1: {len(ws1_buffer)}")
  elif len(ws2_buffer) < MAX_BUFFER_SIZE:
    if len(ws2_buffer) == 0:
      server_status[1] = SERVER_STATUS_BUSY
      ws2_departure_time = clock + get_next_moment(mean_service)
    ws2_buffer.append(clock)
    #print(f"====== Arrival happened in server 2, now buffer length for server 2: {len(ws2_buffer)}")
  else:
    print("arrival dropped because no more capacity")


def departure():
  global ws1_departure_time, ws2_departure_time, ws1_buffer, ws2_buffer
  departing_server = 1 if ws1_departure_time < ws2_departure_time else 2

  #print(f"====== Departure happened for server {departing_server}")
  if departing_server == 1:
    ws1_buffer.pop(0)
    if(len(ws1_buffer) != 0):
        ws1_departure_time = clock + get_next_moment(mean_service)
    else:
      server_status[0] = SEVER_STATUS_IDLE
      ws1_departure_time = sys.float_info.max

  else:
    ws2_buffer.pop(0)
    if(len(ws2_buffer) != 0):
        ws2_departure_time = clock + get_next_moment(mean_service)
    else:
      server_status[1] = SEVER_STATUS_IDLE
      ws2_departure_time = sys.float_info.max

def update_time_avg_stats():
  global clock, area_server_status, time_last_event, SERVER_STATUS_BUSY, area_server_status_s1, area_server_status_s2
  area_server_status += (clock - time_last_event) * (server_status.count(SERVER_STATUS_BUSY)/2)
  area_server_status_s1 += (clock - time_last_event) * server_status[0]
  area_server_status_s2 += (clock - time_last_event) * server_status[1]

  time_last_event = clock


num_of_request = 1

initialize()
while num_of_request <= 1000:
  timing()
  update_time_avg_stats()

  if next_event == "ARRIVAL":
    arrival()
    num_of_request+=1
  elif next_event == "DEPARTURE":
    departure()


print(f"area of server utilization: {area_server_status/clock}")
print(f"area of server utilization for server 1: {area_server_status_s1/clock}")
print(f"area of server utilization for server 2: {area_server_status_s2/clock}")
