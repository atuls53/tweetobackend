from rest_framework import status
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from api.bin.twitter import TWITTER_API
from api.bin.instagram import INSTAGRAM_API

@api_view(['POST'])
def search(request): 
    """
        Api to search keyword on twitter
        accept body in json 
        accecptable args 
        query: search query
        since: 
        until: 
        location: 
        radius: 
    """
    
    twitterapi = TWITTER_API()
    tweets=twitterapi.search_tweets(request.data)
    return JsonResponse(tweets)

@api_view(['GET'])
def insta(request): 
    """
       
    """
    
    instaapi = INSTAGRAM_API()
    instares=instaapi.tagSearch()
    return JsonResponse(instares)

