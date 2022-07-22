import dotenv
import os

dotenv.load_dotenv()

api_key = os.environ["api"]
api_key_secret = os.environ['api_secret']
bearer_token = os.environ['bearer']
access_token = os.environ['access']
access_token_secret = os.environ['access_secret']