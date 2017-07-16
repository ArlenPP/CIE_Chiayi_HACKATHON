##==== for import ====##
import csv

import os
import math
import datetime
import codecs
import re
from dateutil.relativedelta import relativedelta
from raw_data import raw_data
from raw_data import raw_data_bike

##==== start code ====##

##==== function ====##
def move_time ( startLon , startLat , endLon , endLat , moveMethod):
	disLon = abs( startLon - endLon ) * 111
	disLat = abs( startLat - endLat ) * 0.92 * 111
	
	if moveMethod == "bike":
		return ((disLon**2 + disLat**2)**0.5)*2.6
	elif moveMethod == "walk":
		return ((disLon**2 + disLat**2)**0.5)*17

##==== open raw data ====##
bus_raw = open('../raw_data/raw_bus.csv')
bike_raw = open('../raw_data/raw_bike.csv')
attraction_raw = open('../raw_data/raw_attractions.csv')

my_bus = raw_data(bus_raw)
my_attraction_raw = raw_data(attraction_raw)
my_bike = raw_data_bike(bike_raw)

##==== enter where you are ====##
start_x = float(raw_input('Enter what is your lon(x):'))
start_y = float(raw_input('Enter what is your lat(y):'))

##==== enter where you want to go ====##
print ('Here is 20 top hot attractions:')
i = 1
for raw in my_attraction_raw.name:
	print (str(i)+':'+raw)
	i += 1
attractions_number = int(raw_input('Choose the number you want to go:'))
end_x = my_attraction_raw.x[attractions_number-1]
end_y = my_attraction_raw.y[attractions_number-1]
print ('Attraction = '+':'+my_attraction_raw.name[attractions_number-1]+'\n')

##==== find the start bus station ====##
time_true_start = 9999999999999999
bus_number_start = 0

for raw in range(len(my_bus.x)):
	time = move_time(start_x,start_y,my_bus.x[raw],my_bus.y[raw],'walk')
	if(time <= time_true_start):
		time_true_start = time
		bus_number_start = raw

#print time_true_start
print ('The start station'+':'+my_bus.name[bus_number_start])

##==== find the end of attraction ====##

##==== walk from bus to attraction ====##
time_true_end_bus = 99999999999
bus_number_end = 0

for raw in range(len(my_bus.x)):
	time = move_time(end_x,end_y,my_bus.x[raw],my_bus.y[raw],'walk')
	if(time <= time_true_end_bus):
		time_true_end_bus = time
		bus_number_end = raw
print ('The get off station'+':'+my_bus.name[bus_number_end])
between_bus_time = (abs(my_bus.time[bus_number_end]-my_bus.time[bus_number_start]))
time_type_1 = between_bus_time + move_time(start_x,start_y,my_bus.x[bus_number_start],my_bus.y[bus_number_start],'walk') + move_time(end_x,end_y,my_bus.x[bus_number_end],my_bus.y[bus_number_end],'walk')
##==== bike to attraction ====##

time_true_bike = 99999999
time_bike_number = 0
for raw in range(len(my_bike.x)):
	bikeTime_1 = move_time( my_bike.x[raw],my_bike.y[raw],end_x,end_y,'bike' ) + move_time( my_bike.x[raw],my_bike.y[raw],my_bus.x[bus_number_end],my_bus.y[bus_number_end],"walk" )
	if bikeTime_1 <= time_true_bike:
		time_bike_number = raw
		time_true_bike = bikeTime_1
time_type_2 = between_bus_time + time_true_bike

if(time_type_2 > time_type_1):
	print('Time cost ='+str(time_type_1))
	print('walk to start station ='+str(move_time(start_x,start_y,my_bus.x[bus_number_start],my_bus.y[bus_number_start],'walk')))
	print('between station ='+str(between_bus_time))
	print('walk to the attraction = '+str(move_time(end_x,end_y,my_bus.x[bus_number_end],my_bus.y[bus_number_end],'walk')))
else:
	print('Time cost ='+str(time_type_2))
	print('walk to start station ='+str(move_time(start_x,start_y,my_bus.x[bus_number_start],my_bus.y[bus_number_start],'walk')))
	print('between station ='+str(between_bus_time))
	print('walk to the bike station = '+str(move_time(my_bike.x[time_bike_number],my_bike.y[time_bike_number],my_bus.x[bus_number_end],my_bus.y[bus_number_end],'walk')))
	print('ride bike to the attraction = '+ str(move_time(my_bike.x[time_bike_number],my_bike.y[time_bike_number],end_x,end_y,'bike')))







'''
for i in range(len(my_bus.x)):
	print my_bus.name[i]
'''

