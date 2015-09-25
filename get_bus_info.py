import sys
import urllib2
import json
import csv

if __name__=='__main__':
     #key = 'dc6d9908-d5f7-4ae2-a879-75596798f11c'
     #bus = 'M5'
    key = sys.argv[1]
    bus = sys.argv[2]
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (key,bus) 
    request = urllib2.urlopen(url)
    metdata = json.loads(request.read())
    
    busamount = metdata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
    with open(sys.argv[3], 'wb') as csvFile:
        buswriter = csv.writer(csvFile, delimiter = ',')
        buswriter.writerow(("Latitude", "Longtitude", "Stop Name", "Stop Status"))
        for i in range(len(busamount)):
            busLatitude = busamount[i]["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
            busLongitude = busamount[i]["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
            if busamount[i]["MonitoredVehicleJourney"]["OnwardCalls"] != {}:
                stopName = busamount[i]["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["StopPointName"]
                busDistance = busamount[i]["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["Extensions"]["Distances"]["PresentableDistance"]
            else:
                stopName = 'N/A'
                busDistance = 'N/A'
            buswriter.writerow((busLatitude, busLongitude, stopName, busDistance))
