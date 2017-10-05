# This script pulls data from the MTA bus API and prints location of all active buses for a certain line

import os
import sys
import pandas
import pylab as pl
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

# Arguments test
#print("This is the name of the script: ", sys.argv[0] )
#print("Number of arguments: ", len(sys.argv) )
#print("The arguments are: " , str(sys.argv) )

api_key = str(sys.argv[1]).lower()
bus_line = str(sys.argv[2]).upper()

# Fetch data from URL
url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + api_key + '&Version=2&VehicleMonitoringDetailLevel=calls&LineRef=' + bus_line
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

# Check length of list for all buses
all_buses = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

# Print needed data
print('Bus Line :', bus_line)
print('Number of Active Buses :', all_buses)

for i in range(all_buses):
    lati = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longi = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print ('Bus', i, 'is at latitude', lati, 'and longitude', longi)
