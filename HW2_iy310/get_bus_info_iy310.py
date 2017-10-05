# This script displays information on the next stop location of all busses of a given line

import os
import sys
import pandas
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

# Arguments test
print("This is the name of the script: ", sys.argv[0] )
print("Number of arguments: ", len(sys.argv) )
print("The arguments are: " , str(sys.argv) )

# Arguments check
if not len(sys.argv) == 4:
    print ("Invalid number of arguments. Run as: python get_bus_info_iy310.py <API_KEY> <BUS_LINE> <BUS_LINE>.csv")
    sys.exit()

api_key = str(sys.argv[1]).lower()
bus_line = str(sys.argv[2]).upper()

# Set up csv file to write to
fout = open(sys.argv[3], "w")
fout.write("Latitude,Longitude,Stop Name,Stop Status\n")

# Fetch data from URL
url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + api_key + '&Version=2&VehicleMonitoringDetailLevel=calls&LineRef=' + bus_line
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

# Check length of list for all buses
all_buses = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

# print to csv
na = 'N/A'

for i in range(all_buses):
    try:
        lati = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    except:
        lati = na

    try:
        longi = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    except:
        longi = na

    try:
        stop_name = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    except:
        stop_name = na

    try:
        stop_status = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    except:
        stop_status = na

    item_list = [lati, longi, stop_name, stop_status]

    for i in range(len(item_list)):
        if i < len(item_list) - 1:
            fout.write(str(item_list[i]) + ',')
        elif i == len(item_list) - 1:
            fout.write(str(item_list[i]) + '\n')
