from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()

# Set up the email parameters
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
CLIENT_RETURN_CODE = os.getenv('CLIENT_RETURN_CODE')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USERNAME = os.getenv('USERNAME')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                                cache_path="token.txt",
                                                username=f"{USERNAME}" ))
user_id = sp.current_user()["id"]                                                


date = input("Which year do you want to travel? Type in the format, YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
content = response.text


soup = BeautifulSoup(content, "html.parser")
selected_song_list=soup.select("li > #title-of-a-story")
# song_list=selected_song_list.find_all(id="title-of-a-story")
songs_list=[song.getText().strip() for song in selected_song_list]
# print(songs_list)

song_uris=[]
year = date.split("-")[0]

# print(songs_list[0])
results=sp.search(q=f"track:{songs_list[0]} year:{year}",limit=2, type='track')
# pprint.pprint(results)


for song in songs_list:
    results=sp.search(q=f"track:{song} year:{year}", type='track')
    # pprint.pprint(results)
    try:
        uri = results["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist=sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False, collaborative=False, description=f"Play list that is created from the Billboard 100 list of the year {year}")

# for song_uri in song_uris:
#     sp.playlist_add_items(playlist_id=playlist_id["id"], items=song_uri)
#     print("added")
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)