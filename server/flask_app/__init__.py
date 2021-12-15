from json import load
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_app.config.celery import make_celery
from flask_app.models.video import Video
from datetime import timedelta
import os
from bs4 import BeautifulSoup
import requests
from googleapiclient.discovery import build
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379',
    CELERYBEAT_SCHEDULE= {
        'say-every-10-minutes': {
            'task': 'insert_random_video',
            'schedule': timedelta(minutes=10)
        }
    },
    CELERY_TIMEZONE='UTC'
)

celery = make_celery(app)

@celery.task(name='insert_random_video')
def insert_random_video():
    html_text = requests.get('https://www.youtuberandom.com/').text
    soup = BeautifulSoup(html_text, 'lxml')
    video = soup.find('meta', property = 'og:video')
    video_id = video["content"][-11:]

    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY= os.getenv("DEVELOPER_KEY")

    youtube = build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.videos().list(
        part="snippet",
        id=video_id
    )
    response = request.execute()

    # contains everything about the video except the dislikes
    video = response["items"][0]
    video_statistics = requests.get(f"https://returnyoutubedislikeapi.com/Votes?videoId={video['id']}").json()

    data = {
        "video_id" : video["id"],
        "title" : video["snippet"]["title"],
        "channel_name": video["snippet"]["channelTitle"],
        "dislikes": video_statistics["dislikes"]
    }

    Video.create_video(data)

    return 'inserted into the db'

CORS(app)
api = Api(app)
