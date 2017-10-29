# RAC 


from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream

import json
from auth import TwitterAuth

class limit_tweets(StreamListener):

	def limit_reached(self, tweets):


class StdOutListener(StreamListener):

	#event_tweets gets called for every new tweet coming in on the stream

	def event_tweets(self, tweets):

		fhOut.write(tweets)

		tweetsjson = json.loads(tweets)

		text=tweetsjson["text"] #content of tweet
		#print(text) #uncomment as needed

#error handling
 	def event_error(self, status): #prints whatever's going on. Document the errors later
 		print("ERROR")
 		print(status)



class AuthError(Exception):
	def __init__(self, auth_error): 
		self.auth_error = empty_auth?() #if this is true, raise an auth key error
	def __str__(self):
		return repr(self.auth_error)

try:
	raise AuthError(check_auth())
except AuthError as e: 
	print ('Auth file needs all its information (consumer_key, access_token, etc.', e.auth_error)



 if __name__ =='__main__':
 	try: 

 		#store all the tweets in one file or two different files?
 		fhOut = open("all_tweets.json", "a") #append to the file if its less than 2500 records long

 		#listener time
 		listen = StdOutListener()
 		auth = OAuthHandler(TwitterAuth.consumer_key, TwitterAuth.consumer_secret)
		auth.set_access_token(TwitterAuth.access_token, TwitterAuth.access_token_secret


		#connect to Twitter
		stream = Stream(auth, listen)

		#terms
		stream.filter(track["I love you", "f"])	

		except ValueError: 
			print('')

		except KeyboardInterrupt:

			#control c to stop
			pass



fhOut.close()