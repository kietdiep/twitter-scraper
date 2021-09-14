import tweepy
import pandas as pd
import json

consumer_key = "dSVHJRLbOWB5JwySmE3WeaIdu"
consumer_secret = "FhqVe6wPbtrmMJqDuYcJsCL1b8jedyZJXRm5cOBhjjZAFGTNqU"
BEARER = "AAAAAAAAAAAAAAAAAAAAABMhSwEAAAAAG0%2B%2BqKdqrmZoPFRIKcKPnPBvmD0%3D3I3UApK3uPzzPNBZMresVuNpFM34y5DOfDBcchS2DsidgzHCiA"
access_token = "2462026471-MVf0Dyr95WUCfGqqRAHOR3ZTRO8poYcMboHzCTt"
access_token_secret = "sqDqsqqSG0kkh3s2y4H6mPTJv6Ae5SaQsox8fyjSrtH44"


def keywordScrape(keyword):
    tweets = api.search(keyword, count = 100)
    db = pd.DataFrame(columns=['username', 'description', 'location', 'following', 'followers', 'totaltweets', 'retweetcount', 'text', 'hashtags'])
    i = 1
    list_tweets = [tweet for tweet in tweets]
    for tweet in list_tweets:
        username = tweet.user.screen_name
        description = tweet.user.description
        location = tweet.user.location
        following = tweet.user.friends_count
        followers = tweet.user.followers_count
        totaltweets = tweet.user.statuses_count
        retweetcount = tweet.retweet_count
        hashtags = tweet.entities['hashtags']

        try:
            text = tweet.retweeted_status.text
        except AttributeError:
            text = tweet.text
        hashtext = list()
        for j in range(0, len(hashtags)):
            hashtext.append(hashtags[j]['text'])

        # Here we are appending all the extracted information in the DataFrame
        ith_tweet = [username, description, location, following,
                     followers, totaltweets, retweetcount, text, hashtext]
        db.loc[len(db)] = ith_tweet
          
        # Function call to print tweet data on screen
        printtweetdata(i, ith_tweet)
        i = i+1
    filename = 'scraped_tweets.csv'
    db.to_csv(filename)






# -------------------------------- USERNAME SEARCH ------------------------------- #
def userScrape(username, numtweet):
    tweets = api.user_timeline(screen_name=username,count=numtweet)
    db = pd.DataFrame(columns=['username', 'description', 'location', 'following', 'followers', 'totaltweets', 'retweetcount', 'text', 'hashtags'])
    
    i = 1
    list_tweets = [tweet for tweet in tweets]
    for tweet in list_tweets:
        username = tweet.user.screen_name
        description = tweet.user.description
        location = tweet.user.location
        following = tweet.user.friends_count
        followers = tweet.user.followers_count
        totaltweets = tweet.user.statuses_count
        retweetcount = tweet.retweet_count
        hashtags = tweet.entities['hashtags']

        try:
            text = tweet.retweeted_status.text
        except AttributeError:
            text = tweet.text
        hashtext = list()
        for j in range(0, len(hashtags)):
            hashtext.append(hashtags[j]['text'])

        # Here we are appending all the extracted information in the DataFrame
        ith_tweet = [username, description, location, following,
                     followers, totaltweets, retweetcount, text, hashtext]
        db.loc[len(db)] = ith_tweet
          
        # Function call to print tweet data on screen
        printtweetdata(i, ith_tweet)
        i = i+1
    filename = 'scraped_tweets.csv'
    db.to_csv(filename)


# -------------------------------- LOCATION SEARCH ------------------------------- #






# -------------------------------- HASHTAG SEARCH ------------------------------- #
#remember to call scrape later
def hashscrape(words, date_since, numtweet):
    
    #creates DataFrame using pandas
    db = pd.DataFrame(columns=['username', 'description', 'location', 'following', 'followers', 'totaltweets', 'retweetcount', 'text', 'hashtags'])

    tweets = tweepy.Cursor(api.search, q=words, lang="en", since=date_since, tweet_mode='extended').items(numtweet)
    
    i = 1
    list_tweets = [tweet for tweet in tweets]

    for tweet in list_tweets:
        username = tweet.user.screen_name
        description = tweet.user.description
        location = tweet.user.location
        following = tweet.user.friends_count
        followers = tweet.user.followers_count
        totaltweets = tweet.user.statuses_count
        retweetcount = tweet.retweet_count
        hashtags = tweet.entities['hashtags']

        try:
            text = tweet.retweeted_status.full_text
        except AttributeError:
            text = tweet.full_text
        hashtext = list()
        for j in range(0, len(hashtags)):
            hashtext.append(hashtags[j]['text'])

        # Here we are appending all the extracted information in the DataFrame
        ith_tweet = [username, description, location, following,
                     followers, totaltweets, retweetcount, text, hashtext]
        db.loc[len(db)] = ith_tweet
          
        # Function call to print tweet data on screen
        printtweetdata(i, ith_tweet)
        i = i+1
    filename = 'scraped_tweets.csv'
    db.to_csv(filename)

# -------------------------------- Print Function ------------------------------- #
def printtweetdata(n, ith_tweet):
    print()
    print(f"Tweet {n}:")
    print(f"Username:{ith_tweet[0]}")
    print(f"Description:{ith_tweet[1]}")
    print(f"Location:{ith_tweet[2]}")
    print(f"Following Count:{ith_tweet[3]}")
    print(f"Follower Count:{ith_tweet[4]}")
    print(f"Total Tweets:{ith_tweet[5]}")
    print(f"Retweet Count:{ith_tweet[6]}")
    print(f"Tweet Text:{ith_tweet[7]}")
    print(f"Hashtags Used:{ith_tweet[8]}")

# -------------------------------- Main ------------------------------- #

if __name__ == "__main__":
    #myStreamListener = MyStreamListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    #myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

    print("Welcome to the twitter search bot. Please follow instructions below to search for the most relevant tweets for your search")
    inputStr = input("Enter 'k' for keyword, 'u' for username, 'c' for coordinates, '#' for hashtags:, or 'q' to quit: ")
    #fix functionality where you can switch to another input or quit
    while True:
        try:
            if inputStr.lower() == 'k':
                keyword = input("Enter keyword: ")
                #myStream.filter(track=[keyword])
                keywordScrape(keyword)                              
            elif inputStr.lower() == 'u':
                username = input("Enter username: ")
                userScrape(username,numtweet=100)                              # completed
            elif inputStr.lower() == 'c':
                coords = input("Enter coordinates: ")                            # in progressdd
            elif inputStr == '#':
                hashtag = input("Enter hashtag without hashtag symbol: ")
                date_since = input("Enter current date in yyyy-mm-dd: ")
                hashscrape(hashtag, date_since, numtweet = 100)                # completed
            elif inputStr == 'q':
                exit()
            else:
                print("Incorrect input, try again")
        except ValueError:
            print("Invalid input")
            continue





