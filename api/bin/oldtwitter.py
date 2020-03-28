# import tweepy
from searchtweets import ResultStream, gen_rule_payload, load_credentials, collect_results

class TWITTER_API:
    def __init__(self):
        self.premium_search_args = load_credentials(filename="./api/bin/twitter_keys.yaml",
                 yaml_key="search_tweets_api",
                 env_overwrite=False)

    # searchData['query'], searchData['since'], searchData['until'], searchData['location'], searchData['radius']
    def search_tweets(self, searchData):
        rule = gen_rule_payload(searchData['query'],
                        from_date=searchData['since'], #UTC 2017-09-01 00:00
                        to_date=searchData['until'],#UTC 2017-10-30 00:00
                        results_per_call=100)
        
        tweets = collect_results(rule, max_results=50, result_stream_args=self.premium_search_args)
        print(tweets)

        # for tweet in tweets:
        #     filterData=self.serializedata(tweet)
        #     tweet_array.append(filterData)
        
        # return {'tweets': tweet_array, 'sinceId': tweets.since_id, 'max_id': tweets.max_id, 'tweet_count': tweets.count}
    
    def serializedata(self, tweet):
        # user = tweet.user if tweet.user else tweet.author
        data = {
            'date': tweet.created_at.date(),
            'time': tweet.created_at.time(),
            'screenName': tweet.user.screen_name,
            'name': tweet.user.name,
            'tweetId': tweet.id,
            'tweet': tweet.text,
            'retweet': tweet.retweet_count,
            'source': tweet.source,
            'likes':'N.A.',
            'user':{
                'followers': tweet.user.followers_count,
                'follows': tweet.user.friends_count,
                'favourities': tweet.user.favourites_count,
                'location': tweet.user.location,
                'memberSince': tweet.user.created_at.date()
            }
        }
        return data

    


    

    # if sinceId != '0':
        #     tweets=self.api.search(q=searchData.query, count=100, result_type='recent', since_id=0)
        # elif maxId != '0':
        #     tweets=self.api.search(q=searchData.query, count=100, result_type='recent', max_id=0) 
        # else: