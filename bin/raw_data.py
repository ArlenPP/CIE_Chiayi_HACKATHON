import csv
import os

class raw_data:
	def __init__(self,file):

		self.name = []
		self.y = []
		self.x = []
		self.time = []

		for row in csv.DictReader(file):
			self.name.append(row['name'])
			self.y.append(float(row['y']))
			self.x.append(float(row['x']))
			self.time.append(float(row['a']))
class raw_data_bike:
	def __init__(self,file):

		self.name = []
		self.y = []
		self.x = []
		self.time = []
		self.nearestBus = []

		for row in csv.DictReader(file):
			self.name.append(row['name'])
			self.y.append(float(row['y']))
			self.x.append(float(row['x']))
			self.time.append(float(row['a']))
			self.nearestBus.append(int(row['nearestBus']))