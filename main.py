import requests
from secrets import client
from utils import get_game_id, get_timestamp, download_clip, get_todays_date
import os
from channels import channels
base_url = 'https://api.twitch.tv/helix/clips'

number_of_clips = 3

for channel in channels:
    game = channel['game']
    game_id = get_game_id(game)
    
    timestamp = get_timestamp(hours_ago=24)
    date = str(get_todays_date())
    game_folder = f'clips/{game.replace(":", "")}'

    if not os.path.isdir(game_folder):
        os.makedirs(game_folder)
    folder = f'{game_folder}/{date}'
    
    if not os.path.isdir(folder):
        os.makedirs(folder)    
    
    request = requests.get(f'{base_url}?game_id={game_id}&started_at={timestamp}&first=3', headers={
        'Client-ID': client['ID']
    })

    clips = request.json()['data']

    for clip in clips:
        title = clip['title']
        download_clip(clip['thumbnail_url'], f"{folder}/{title}.mp4")
        print(title)

    #top_clip = clips[0]
    #title = top_clip['title']
    #download_clip(top_clip['thumbnail_url'], f"{folder}/{title}.mp4")