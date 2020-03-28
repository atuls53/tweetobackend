from instagram.client import InstagramAPI

class INSTAGRAM_API:
    def __init__(self):
        access_token = "YOUR_ACCESS_TOKEN"
        client_secret = "YOUR_CLIENT_SECRET"
        self.api = InstagramAPI(access_token=access_token, client_secret=client_secret)

    def tagSearch(self):
        user, next_ = self.api.user_search("india", 10, "28.7041", "77.1025", "1539993600", "1540357631")
        for us in user:
            print media.caption.text