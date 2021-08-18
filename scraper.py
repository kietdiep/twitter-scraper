import tweepy
import json

consumer_key = "dSVHJRLbOWB5JwySmE3WeaIdu"
consumer_secret = "FhqVe6wPbtrmMJqDuYcJsCL1b8jedyZJXRm5cOBhjjZAFGTNqU"
BEARER = "AAAAAAAAAAAAAAAAAAAAABMhSwEAAAAAG0%2B%2BqKdqrmZoPFRIKcKPnPBvmD0%3D3I3UApK3uPzzPNBZMresVuNpFM34y5DOfDBcchS2DsidgzHCiA"
access_token = "2462026471-MVf0Dyr95WUCfGqqRAHOR3ZTRO8poYcMboHzCTt"
access_token_secret = "sqDqsqqSG0kkh3s2y4H6mPTJv6Ae5SaQsox8fyjSrtH44"

class MyStreamListener(tweepy.StreamListener):
    filecount = 1
    tweetcount = 1
    def on_status(self, status):
        data = {}
        data['time'] = str(status.created_at)  
        data['username'] = status.user.screen_name
        data['coordinates'] = str(status.coordinates)
        data['retweet_count'] = str(status.retweet_count)
        data['favorite_count'] = str(status.favorite_count)
        data['hashtags'] = str(status.entities.get('hashtags'))

        jsonString = json.dumps(data)
        jsonFile = open('stored_tweets/tweets' + str(self.filecount) + '.json','a+')
        jsonFile.write(jsonString)
        self.tweetcount +=1 
        if self.tweetcount == 100:
            jsonFile.close()
            self.filecount+=1
            self.tweetcount = 1

    def on_error(self, status_code):
        if status_code == 420:
            return False
    
        
if __name__ == "__main__":
    myStreamListener = MyStreamListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

    myStream.filter(track=['donald trump', 'bernie sanders'])
    #will later implement giving keywords to filter for to track



