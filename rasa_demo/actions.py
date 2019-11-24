from rasa_sdk import Action, Tracker
from typing import Any, Text, Dict, List
from apixu.client import ApixuClient

import requests

class ActionWeather(Action):
	def name(self):
		return 'action_weather'
		
	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		params = {
  			'access_key': 'api_key',
  			'query': loc
		}
		api_result = requests.get('http://api.weatherstack.com/current', params)
		api_response = api_result.json()
		res = api_response['current']['temperature']
		print(loc,res)
		response = "The temperature in {} is {} degrees celsius.".format(loc,res)
		dispatcher.utter_message(response)