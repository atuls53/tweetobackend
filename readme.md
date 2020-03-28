# To run app

- virtualenv -p python3 tweetSearchEnv
- source tweetSearchEnv/bin/activate
- pip install -r requirements.txt
- daphne -b 0.0.0.0 -p 8000 tweetapp.asgi:application


# To deploy 
- git push heroku master