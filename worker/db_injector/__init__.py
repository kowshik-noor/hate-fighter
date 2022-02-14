from flask import Flask
from json import load
from db_injector.video import Video
from celery import Celery
from datetime import timedelta
import os
from bs4 import BeautifulSoup
import requests
from googleapiclient.discovery import build

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


app = Flask(__name__)

app.config.update(
    CELERY_BROKER_URL='redis://redis:6379',
    CELERY_RESULT_BACKEND='redis://redis:6379',
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

