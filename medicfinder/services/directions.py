# #Python Get Directions Script

# #import statements
# from googlemaps import Client
# from HTMLParser import HTMLParser
# from sys import argv
# import json

# class MLStripper(HTMLParser):
#     def __init__(self):
#         self.reset()
#         self.fed = []
#     def handle_data(self, d):
#         self.fed.append(d)
#     def get_data(self):
#         return ''.join(self.fed)

# class GoogleDirection():
#     def strip_tags(html):
#         s = MLStripper()
#         s.feed(html)
#         return s.get_data()


# #create GoogleMaps object
#     api_key = 'AIzaSyCy7LFUt1ss4Riedr0gmed9IHvth0qbuY8'
#     mapService = Client(api_key)

#     # Geocoding and address
#     geocode_result = mapService.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
#     # print json.dumps(geocode_result, indent=4)

#     # Look up an address with reverse geocoding
#     reverse_geocode_result = mapService.reverse_geocode((40.714224, -73.961452))
#     # print json.dumps(reverse_geocode_result, indent=4)

#     #get directions from google
#     directions = mapService.directions('lagos', 'romania')
#     print json.dumps(directions, indent=4)
#     #print each step in directions to console
#     # for step in directions[0]['legs'][0]['steps']:
        # print strip_tags(step['html_instructions'])



from googleplaces import GooglePlaces, types, lang
from hospital.models import HospitalDirection
import json

def save_hospital(query):
    for item in query:
        item.get_details()
        print item.formatted_address
        try:
            hospital = HospitalDirection.objects.get(name=item.name, formatted_address=item.formatted_address)
        except Exception, e:
            new_hospital = HospitalDirection(name=item.name, formatted_address=item.formatted_address)
            # print hospital
            new_hospital.save()
            continue
    return 'done'



class HospitalDetail():
        
    YOUR_API_KEY = 'AIzaSyCy7LFUt1ss4Riedr0gmed9IHvth0qbuY8'
    google_places = GooglePlaces(YOUR_API_KEY)

    # You may prefer to use the text_search API, instead.
    query_result = google_places.nearby_search(
            location='Lagos', keyword='hospital', lat_lng=None,
            radius=2000, types=[types.TYPE_HOSPITAL])
    save_hospital(query_result.places)
    # print query_result.places

    # print query_result.html_attributions


    # if query_result.has_attributions:
    #     print query_result.html_attributions

    # for place in query_result.places:
    #   Returned places from a query are place summaries.
        # print dir(place)
        # print place.geo_location
        # print place.place_id

        # The following method has to make a further API call.
        # place.get_details()
        # Referencing any of the attributes below, prior to making a call to
        #get_details() will raise a googleplaces.GooglePlacesAttributeError.
        # print json.dumps(place.details, indent=4) # A dict matching the JSON response from Google.
        # print place.local_phone_number
        # print place.international_phone_number
        # print place.website
        # print place.url
        # print place.details['formatted_address']