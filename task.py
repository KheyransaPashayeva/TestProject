from celery import Celery
from celery.schedules import timedelta
from bot import Browser


app = Celery('bot')


@app.task
def instabot(link, username, password):
    Browser(link, username, password)

app.conf.beat_schedule = {
    'run-bot-every-1-minutes':{
        'task': 'bot.instabot',
        'args': ('link','username','password'),
        'schedule' : timedelta(minutes=1)
    }
}