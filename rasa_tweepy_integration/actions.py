from rasa_sdk import Action, Tracker
from typing import Any, Text, Dict, List
from apixu.client import ApixuClient

import tweepy
import pandas as pd

import requests

class ActionTweepy(Action):
	def name(self):
		return 'action_tweepy'	
	def run(self, dispatcher, tracker, domain):
		u,t,c=[],[],[]
		auth = tweepy.OAuthHandler('GTOFwH0XyYEnJcFK7aymzwXUD','yJBqo2YuEGL9amrlluJqUVjs4xgvktnX3ct54GODDsp3gTQvos')
		auth.set_access_token('1195378945828376577-ztJDNTFENMNZo37xq5S9oOax4xOs4W','rJvIgEJHeCoNlLV4uNw852dM3EQAztl503BuJ6ocorImV')
		api = tweepy.API(auth)
		for tweet in tweepy.Cursor(api.search, q='#datascience',lang="en").items(10):
			u.append(tweet.user.name)
			t.append(tweet.text.encode('utf-8'))
			c.append(tweet.created_at)
		print(u,t,c)
		for i in range(len(u)):
		 	response = "{} : {} by {} at {}.\n".format(i+1,t[i],u[i],c[i])
		 	dispatcher.utter_message(response)


#python -m rasa_sdk --actions actions.