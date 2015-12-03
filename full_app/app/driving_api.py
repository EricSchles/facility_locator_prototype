#comes from here: http://stackoverflow.com/questions/17267807/python-google-maps-driving-time
#travel api docs: https://developers.google.com/maps/documentation/directions/intro#traffic-model
#distance api docs: https://developers.google.com/maps/documentation/distance-matrix/intro?hl=en
import simplejson, urllib
import pickle
api_key = pickle.load(open("google_driving.pickle","r"))
orig_coord = "9 Poplar Court, Great Neck, NY, 11024"
dest_coord = "52 Centre Street, New York, NY, 10007"
print str(orig_coord)
url = "https://maps.googleapis.com/maps/api/directions/json?origin={0}&destination={1}&mode=driving&language=en&key={2}".format(str(orig_coord),str(dest_coord),str(api_key))
result= simplejson.load(urllib.urlopen(url))
print result
#driving_time = result['rows'][0]['elements'][0]['duration']['value']
