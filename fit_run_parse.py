import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from datetime import datetime as dt
from fitparse import FitFile

class FitObject:
    
    def __init__(self, file:FitFile):
        self.file = file
        self.names = []
        self.heart_rates = []
        self.distances = []
        self.times = []
        self.hours = []
        self.minutes = []
        self.seconds = []
        self.mileage = []
        self.day_time = []
        
        self.parse_records()
        self.to_mileage()
        self.calculate_time()
    
        
    def parse_records(self):
        self.index = 0  # initialize index counter
        
        for message in self.file.get_messages("record"):
            for data in message:
                #print(data.name, " : ", data.value)
                
                if data.name == "timestamp":
                    self.hours.append(data.value.hour)
                    self.minutes.append(data.value.minute)
                    self.seconds.append(data.value.second)
                
                elif data.name == "distance":
                    self.distances.append(data.value.__round__(2))
                    
                elif data.name == "heart_rate":
                    self.heart_rates.append(data.value)
                    
                else:
                    pass
                
    def to_mileage(self):
        
        for value in self.distances:
            calc = value / 1609.344
            self.mileage.append(calc)
            
            
    def calculate_time(self):
        
        for i in range(len(self.distances)):
            self.day_time.append((self.hours[i] * 3600) + (self.minutes[i] * 60) + (self.seconds[i]))
        
