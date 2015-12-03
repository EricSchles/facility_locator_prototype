#comes from here: http://stackoverflow.com/questions/17267807/python-google-maps-driving-time
#travel api docs: https://developers.google.com/maps/documentation/directions/intro#traffic-model
#distance api docs: https://developers.google.com/maps/documentation/distance-matrix/intro?hl=en
import simplejson, urllib
orig_lng, orig_lat = [40.7127,-74.0059]
dest_lng, dest_lat = [40.7135,-74.0017]

orig_coord = orig_lat, orig_lng
dest_coord = dest_lat, dest_lng
url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&sensor=false".format(str(orig_coord),str(dest_coord))
result= simplejson.load(urllib.urlopen(url))
print result
#driving_time = result['rows'][0]['elements'][0]['duration']['value']
