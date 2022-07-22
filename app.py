import tweepy
import os
import random
import time
import config

authenticator = tweepy.OAuthHandler(config.api_key,config.api_key_secret)
authenticator.set_access_token(config.access_token,config.access_token_secret)

api = tweepy.API(authenticator,wait_on_rate_limit=True)
client = tweepy.Client(config.bearer_token, config.api_key, config.api_key_secret, config.access_token, config.access_token_secret)


def media_reply(text):
    image = '/app/file_images/'+str(random.choice(os.listdir('/app/file_images/')))
    media = api.media_upload(image)
    api.update_status(status='',media_ids = [media.media_id_string],in_reply_to_status_id=text,auto_populate_reply_metadata=True)

my_id = int(api.verify_credentials().id_str)
mention_id = 1
initialisation_resp = client.get_users_mentions(my_id)
if initialisation_resp.data != None:
    mention_id = initialisation_resp.data[0].id

words = ['attack']

while True:
    mentions = api.mentions_timeline(since_id=mention_id)
    for mention in mentions:
        print("Mention tweet found")
        print(f"{mention.author.screen_name} - {mention.text}")
        mention_id = mention.id
        if mention.author.id != my_id:
            if True in [word in mention.text.lower() for word in words]:
                try:
                    print("Attempting to reply...")
                    media_reply(mention.id)
                    print('replied successfully')
                except Exception as exc:
                    print(exc)


    time.sleep(30)
