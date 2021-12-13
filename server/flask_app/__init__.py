from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_app.config.celery import make_celery
from datetime import timedelta

app = Flask(__name__)

app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379',
    CELERYBEAT_SCHEDULE= {
        'say-every-10-seconds': {
            'task': 'return_something',
            'schedule': timedelta(seconds=10)
        }
    },
    CELERY_TIMEZONE='UTC'
)

celery = make_celery(app)

@celery.task(name='return_something')
def return_something():
    print('something')
    return 'something'

CORS(app)
api = Api(app)
