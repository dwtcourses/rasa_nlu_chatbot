#Phoenix magicianGirl 23/10/2018
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet, AllSlotsReset
import requests
import json
from random import randint
import datetime
import os




class ActionPlaceSearch(Action):
    def name(self):
        #define the name of the action		
        return 'action_POI'

    def run(self, dispatcher, tracker, domain):
        #retrieve slot values	
        query = tracker.get_slot('query')
        radius = tracker.get_slot('number')		

        #retrieve google api key		
        key = 'AIzaSyBM04t6DckU-P98B233fGSGLzX5HQTSJrw'
		
        #get user's current location		
        #get_origin = requests.post(
            #"https://www.googleapis.com/geolocation/v1/geolocate?key={}".format(key)).json()
        origin_lat = '-26.0960025'#get_origin['location']['lat']
        origin_lng = '28.0385992,17z'#get_origin['location']['lng']
				
        #look for a place using all the details
        place = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius={}&type={}&key={}'.format(origin_lat, origin_lng, radius, query, key)).json()
        if len(place['results'])==0:
            dispatcher.utter_message("Sorry, I didn't find anything")
            return [SlotSet('location_match', 'none')]
        else:
            for i in place['results']:
                if 'rating' and 'vicinity' in i.keys():				
                    name = i['name']
                    rating = i['rating']
                    address = i['vicinity']
                    if i['opening_hours']['open_now']==True:
                        opening_hours = 'open'
                    else:
                        opening_hours = 'closed'
                    break
            speech = "I found a {} called {} based on your specified parameters.".format(query, name)
            dispatcher.utter_message(speech) #send the response back to the user	
            return [SlotSet('location_match', 'one'), SlotSet('rating', rating), SlotSet('address', address), SlotSet('opening_hours', opening_hours)] #set returned details as slots



