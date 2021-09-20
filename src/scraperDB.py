import tweepy
from datetime import date
import sqlite3


consumer_key = "dSVHJRLbOWB5JwySmE3WeaIdu"
consumer_secret = "FhqVe6wPbtrmMJqDuYcJsCL1b8jedyZJXRm5cOBhjjZAFGTNqU"
BEARER = "AAAAAAAAAAAAAAAAAAAAABMhSwEAAAAAG0%2B%2BqKdqrmZoPFRIKcKPnPBvmD0%3D3I3UApK3uPzzPNBZMresVuNpFM34y5DOfDBcchS2DsidgzHCiA"
access_token = "2462026471-MVf0Dyr95WUCfGqqRAHOR3ZTRO8poYcMboHzCTt"
access_token_secret = "sqDqsqqSG0kkh3s2y4H6mPTJv6Ae5SaQsox8fyjSrtH44"


class Scraper():
    def __init__(self, filter, searchTerm):
        self.dbInitialize()
        self.filter = filter
        self.searchTerm = searchTerm
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        self.completeScrape(api)

    
    def dbInitialize(self):
        self.conn = sqlite3.connect('twitterInfo.db')
        self.c = self.conn.cursor()

        self.c.execute("""CREATE TABLE IF NOT EXISTS Tweet (
        Username TEXT,
        Description TEXT,
        Tweet TEXT,
        Location TEXT,
        Following TEXT,
        Followers TEXT,
        Totaltweets TEXT,
        Retweetcount TEXT,
        Hashtags TEXT
        )""")

    

    def completeScrape(self, api):
        if self.filter == 'k':
            tweets = api.search(self.searchTerm, count = 100)
        elif self.filter == 'u':
            tweets = api.user_timeline(screen_name=self.searchTerm,count=100)
        elif self.filter == 'c':
            pass
        elif self.filter == '#':
            today = date.today()
            tweets = tweepy.Cursor(api.search, q=self.searchTerm, lang="en", since=today.strftime("%Y-%m-%d"), tweet_mode='extended').items(100)
        
        list_tweets = [tweet for tweet in tweets]
        for tweet in list_tweets:
            username = tweet.user.screen_name
            description = tweet.user.description
            location = tweet.user.location
            following = str(tweet.user.friends_count)
            followers = str(tweet.user.followers_count)
            totaltweets = str(tweet.user.statuses_count)
            retweetcount = str(tweet.retweet_count)
            hashtags = tweet.entities['hashtags']
            try:
                if self.filter == '#':
                    text = tweet.retweeted_status.full_text
                else:  
                    text = tweet.retweeted_status.text
            except AttributeError:
                if self.filter == '#':
                    text = tweet.full_text
                else:
                    text = tweet.text
            hashtext = list()
            for j in range(0, len(hashtags)):
                hashtext.append(hashtags[j]['text'])
            hashStr = ','.join(str(e) for e in hashtext)
            self.c.execute("INSERT INTO Tweet VALUES (:username, :description, :Tweet, :location, :following, :followers, :totaltweets, :retweetcount, :hashtags)", {'username' : username, 'description':description, 'Tweet': text, 'location':location, 'following':following, 'followers':followers, 'totaltweets':totaltweets, 'retweetcount':retweetcount, 'hashtags':hashStr})
        self.conn.commit()
        self.conn.close()




