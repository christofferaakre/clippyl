import requests
from secrets import client
from datetime import datetime, timedelta
import urllib
import os

url = 'https://api.twitch.tv/helix/games?'

def get_game_id(game: str):
    """
    Uses the Helix API to get the id of a game
    """
    request = requests.get(f'{url}name={game}', headers={
        'Client-ID': client['ID']
    })
    return request.json()['data'][0]['id']

def get_timestamp(hours_ago: int = 24):
    """
    Gets an ISO timestamp the specified number of hours ago 
    """
    return f'{(datetime.utcnow() - timedelta(hours = hours_ago)).isoformat()}Z'

def get_todays_date():
    return datetime.utcnow().date()

def download_clip(thumbnail_url: str, location: str):
    """
    Use a little trick to download a twitch clip using the thumbnail url and saves it in the given location
    """
    clip_url = thumbnail_url.split("-preview")[0] + '.mp4'
    return urllib.request.urlretrieve(clip_url, location)