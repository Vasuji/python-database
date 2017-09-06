# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 19:34:00 2015

@author: dibakarsigdel
"""




import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

#address = "Pondicherry University"

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    print json.dumps(js, indent=4)

   

    print"================================================"
    PlaceId = js["results"][0]["place_id"]
    print "place_id is ", PlaceId







