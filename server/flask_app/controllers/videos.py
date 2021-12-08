from flask_app import app, api, Resource
from bs4 import BeautifulSoup
import requests
import os
from googleapiclient.discovery import build
from dotenv import load_dotenv
from flask_app.models.video import Video

load_dotenv()

class RandomVideo(Resource) :
    def get(self):
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
            part="snippet,statistics",
            id=video_id
        )
        response = request.execute()

        video = response["items"][0]

        data = {
            "video_id" : video["id"],
            "title" : video["snippet"]["title"],
            "channel_name": video["snippet"]["channelTitle"],
            'dislikes': video["statistics"]["dislikeCount"]
        }

        return Video.create_video(data)