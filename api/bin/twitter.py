import tweepy
from django_eventstream import send_event

class TWITTER_API:
    def __init__(self):
        consumer_key='7HXAUC0mMi1Ileefz3NgLXu17'
        consumer_secret='UXkoWepv93JOcESa4TE4K3Pa4vLuIrcAIGId44mZOwaWdXjcfw'

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.api = tweepy.API(auth)

    def search_tweets(self, searchData):
        
        repeat_search = True
        max_id = None
        returnDict = {'tweets': [], 'tweet_count': 0, 'status':''}

        while repeat_search:
            tweets=self.api.search(q=searchData['query'], geocode=searchData['geocode'], until=searchData['until'], lang='en', count=100, result_type='recent', max_id=max_id)
            if tweets:
                if len(tweets)<100: repeat_search = False
                max_id=tweets.max_id

                returnDict['status'] = 'DONE' if len(tweets)<100 else 'IN_PROGRESS'

                returnArray=[]
                # Searializing data as per need and appending into return tweet array 
                for tweet in tweets:
                    filterData=self.serializedata(tweet)
                    returnArray.append(filterData)
                
                returnDict['tweets'] = returnArray
                returnDict['tweet_count'] = len(returnArray)
                send_event(searchData['channel'], 'data', returnDict)
            else:
                repeat_search = False
                returnDict['status'] = 'DONE'
                returnDict['tweets'] = [] 
                send_event(searchData['channel'], 'data', returnDict)      
        
        return {'meassage': 'Tweet fetching done'}
    
    def serializedata(self, tweet):
        # user = tweet.user if tweet.user else tweet.author
        data = {
            'dateTime': tweet.created_at,
            'date': tweet.created_at.date(),
            'time': tweet.created_at.time(),
            'screenName': tweet.user.screen_name,
            'name': tweet.user.name,
            'tweetId': tweet.id_str,
            'tweet': tweet.text,
            'retweet': tweet.retweet_count,
            'source': tweet.source,
            'likes': tweet.favorite_count,
            'user':{
                'followers': tweet.user.followers_count,
                'follows': tweet.user.friends_count,
                'favourities': tweet.user.favourites_count,
                'location': tweet.user.location,
                'memberSince': tweet.user.created_at.date()
            }
        }
        return data