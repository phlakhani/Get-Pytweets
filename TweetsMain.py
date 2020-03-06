from tweepy import OAuthHandler
import twitter_tokens
from tweepy import API
from tweepy import Cursor
import pandas as pd
import numpy as np
import gettweetgui

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

    AnalyzedTweet = TweetAnalyzer()
    df = AnalyzedTweet.tweets_to_dataframe(actualtweet)
    usertweet = df.head(30)
    s=str(usertweet)
    return s
