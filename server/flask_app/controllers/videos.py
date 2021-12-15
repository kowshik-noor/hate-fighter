from flask_app import app ,api, Resource
from flask_app.models.video import Video
from datetime import datetime, date
import json

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

class RandomVideo(Resource) :
    def get(self):
        video = Video.random_video().__dict__
        video_json = json.dumps(video, default=json_serial)

        return video_json



