import json
import sys
import urllib2



if __name__=='__main__':
    key = 'dc6d9908-d5f7-4ae2-a879-75596798f11c'
    bus = 'M5'
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' %(key,bus) 
    request = urllib2.urlopen(url)
    metdata = json.loads(request.read())
    print "Bus Line : %s" % sys.argv[2]

   
    busamount = metdata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

    print "Number of Active Buses : %d" % len(busamount)
    
    count = 0
    for i in busamount:
         
         latitude  = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
         longitude = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
         print "Bus %d latitude is at %f and longitude is %f" %(count,latitude,longitude) 
         count += 1   
