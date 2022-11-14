import os

import tweepy


def tweet(message: str) -> None:
    auth = tweepy.OAuthHandler(
        os.getenv('API_KEY'), os.getenv('API_SECRET_KEY'))
    auth.set_access_token(os.getenv('ACCESS_TOKEN'),
                          os.getenv('SECRET_ACCESS_TOKEN'))
    print(message)
    tweepy.API(auth).update_status(message)
