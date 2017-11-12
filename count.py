import tweepy

f = open("tw.config","r")
cKey = f.readline()
cSecret = f.readline()
aToken = f.readline()
aTokenSecrect = f.readline()

auth = tweepy.OAuthHandler(ckey, cSecret)
auth.set_access_token(aToken, aTokenSecret)
api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
	print tweet.txt
