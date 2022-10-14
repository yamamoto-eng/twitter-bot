import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

client = tweepy.Client(
    os.getenv("BEARER_TOKEN"),
    os.getenv("API_KEY"),
    os.getenv("API_KEY_SECRET"),
    os.getenv("ACCESS_TOKEN"),
    os.getenv("ACCESS_TOKEN_SECRET"),
)
