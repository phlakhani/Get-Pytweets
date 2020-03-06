#from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
#from tweepy import Stream
import twitter_tokens
from tweepy import API
from tweepy import Cursor

import pandas as pd
import numpy as np
import gettweet


###""""   Commenting twitter code

class demo():
    def demofun(self):
        return "6"



class twitter_client():
    def __init__(self,twitter_user=None):
        self.auth=TwitterAuthenticator().authenticate_twitter_app()
        self.twitterclient=API(self.auth)
        self.twitter_user=twitter_user
        #print("init done")

    def get_twitterclient_api(self):
        return self.twitterclient

    def get_user_timeline_tweet(self,num_tweet):
        tweets=[ ]  # array to collect tweets
        for tweet in Cursor(self.twitterclient.user_timeline, id=self.twitter_user).items(num_tweet):
            #print(tweet)
            #print('dfdf')
            tweets.append(tweet)
        return tweets





class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_tokens.CONSUMER_KEY, twitter_tokens.CONSUMER_SECRET)
        auth.set_access_token(twitter_tokens.ACCESS_TOKEN, twitter_tokens.ACCESS_TOKEN_SECRET)
        return auth
"""

class TwitterStream():
    #class for streaming  and processing live tweets

    def __init__(self):
       self.twitter_authenticator=TwitterAuthenticator()

    def stream_tweets(self, tweetfile, Keyword):
        #this handles twitter authenication n connection to twitter streaming api

        Listener = StdoutListner(tweetfile)  #my changes, before tweet file was not in arguments of StdourLister()

        auth=self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, Listener)
        data = stream.filter(track=Keyword)




class StdoutListner(StreamListener):

    # basic listener class that prints received tweets to stdout
    def __init__(self, tweetfile):
        self.tweetfile = tweetfile

    def on_data(self, data):
        try:
            print(data)
            with open(self.tweetfile, 'a') as file:
                        file.write(data)
            return True
        except BaseException as e:
                print("Error on data: %s" % str(e))
        return True

    def on_error(self, status):
        if status==420:
            return False   #returning fals on_data method in case rate limit occurs
        print(status)

"""

class TweetAnalyzer():
    # functinality for analyzing and categorizing from occurs
    def tweets_to_dataframe(self, actualtweet):        #convert whole actual tweet string to data frame
       df=pd.DataFrame(data=[i.text for i in actualtweet], columns=['Current Tweets']) # dataframe will get data string and extract 'text' content
       df['Tweeted at']=np.array([i.created_at for i in actualtweet]) # create column 'created at' in numpy array  for each 10 tweets
       #df['Place'] = np.array([i.place for i in actualtweet])

       return df


def myfun(value):

    client = twitter_client()
    api = client.get_twitterclient_api()
    actualtweet = api.user_timeline(screen_name=value, count=5)  # in above line user_timeline is is default method, so aslo arguments screen_name,count
    # print(actualtweet)
    AnalyzedTweet = TweetAnalyzer()
    df = AnalyzedTweet.tweets_to_dataframe(actualtweet)

    # print(dir(actualtweet[0]))  # it shows what piece of information exactly we can get from tweet like screen_name,user, likes, id, text etc.
    # print(actualtweet[0].text) #  shows  only text of 1st tweet
    usertweet = df.head(30)
    #print(type(usertweet))
    s=str(usertweet)
    #print(type(s))
    #print(usertweet)  # gives first 10 line in generated datafrmae
    #demo1=demo()
    #z=demo1.demofun()
    #print(z)
    return s

#    twitter_streamer=TwitterStream()
#    twitter_streamer.stream_tweets(tweetfile,Keyword)

#mytext1='narendramodi'
#print(myfun(mytext1))








