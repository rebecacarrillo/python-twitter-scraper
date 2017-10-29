#RAC

#lets get these tweets in a csv (yeehaw)


import json
import time
import datetime
import os
import random 
import sys
import codecs



queries=["I love you", "f"]


outputDir = "tweets_output/"
#if it doesn't exist already
os.system("mkdir -p %s"%(outputDir))


fhLog = codes.open ("LOG.txt", 'a', 'UTF-8')
def logPrint(s):
	fhLog.write("%s\n"%s)
	print(s)


class Tweet:

	 def __init__(self): 
	 	self.keywords=[]
	 	self.links=["", "", ""]
	 	self.lang=""
	 	self.lanfConf=""


	 	@staticmethod

	 	# column headers
	 	def columnHeaders():
	 		row = "\"\"".join(("URL", "Keywords", 
	 			"Keyword Count", "DateTime", 
	 			"Favorite Count", "Retweet", 
	 			"Lang", "LinkCount", 
	 			"Link1", "Link2", "Link3", 
	 			"Author", "Text", "Followers","Friends",
	 			"Location","Timezone","UTC Offset"))
	 		row = "\"%s\"n"%row
	 		return row


	 	def csvRow(self):
	 		row = "\"\t\"".join((
	 			str(self.url),
			",".join(self.keywords),
			str(len(self.keywords)),
			#str(datetime.datetime.fromtimestamp(self.date).strftime('%Y-%m-%d %H:%M:%S')),
			str(self.date),
			str(self.favorite),
			str(self.retweet),
			str(self.lang),
			str(self.urlCount),
			self.links[0],
			self.links[1],
			self.links[2],
			self.author,
			self.clean_text(),
			str(self.followers),
			str(self.friends),
			self.location,
			self.timezone,
			str(self.utc)
	 			))

	 	row = "\"%s\"\n"%row
	 	return row

	def parse(self, json):
	self.url="http://twitter.com/{0}/status/{1}".format(json["user"]["id_str"],json["id_str"])
			self.date=json["created_at"]
			self.favorite=json["favorite_count"]
			self.retweet=json["retweet_count"]
			self.author=json["user"]["screen_name"]
			#"%s - Twitter"%json["trackback_author_name"] 
			self.text=json["text"]
			
			self.lang=json["lang"]
			
			self.followers=json["user"]["followers_count"]
			self.friends=json["user"]["friends_count"]
			self.location=json["user"]["location"]  if json["user"]["location"] else ""
			self.timezone=json["user"]["time_zone"] if json["user"]["time_zone"] else ""
			self.utc=json["user"]["utc_offset"]  if json["user"]["utc_offset"] else ""
			
			#Links
			text = self.text
			self.urlCount = text.count("http://") + text.count("https://")

			count=0
			words=text.split()
			for w in words:
				if w.count("http://") or w.count("https://"):
					w=w[(w.find("http")):]
					w=w.strip("():!?. \t\n\r")
					if count>2:
						self.links[2]=self.links[2]+","+w
					else:
						self.links[count]=w
					count=count+1
						
	def __hash__(self):
		return hash(self.url, self.location)

	def __eq__(self, other):
		return (self.url)==(self.url)


allTweets={}
def parse(tweet):

	tweet=Tweet()
	tweet.parse(tweet)

	if not (tweet.url in allTweets):
		text = tweet.text.lower()
		for query in queries: 
			if query in text: 
				tweet.keywords.append(query)

			if len(tweet.keywords) > 0:
			all tweets[tweet.url] = tweet

fhOverall = None

for file in sys.argv[1:]: 
	print(file)
	fhb = codecs.open(file, "r")

	firstLine = fhb.readline()

	tweetsjson=json.loads(firstLine)
	if "statuses" in tweetsjson:
		for tweet in tweetsjson["statuses"]: 
			parse(tweet)

	else: 

		parse(tweetsjson)
		for line in fhb: 
			parse(json.loads(line))

fhb.close()


fhOverall=codecs.open(outputDir+"overall_%s.csv"%int(time.time()), "w", "UTF-8")
fhOVerall.write(Tweet.columnHeaders())
for url in allTweets:

	tweet=allTweets[url]
	fh.Overall.write(tweet.csvRow())


fhOverall.close()


logPrint ("\nComplete")

fhlog.close()
