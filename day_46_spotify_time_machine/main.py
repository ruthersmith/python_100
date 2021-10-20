from bs4 import BeautifulSoup
import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import datetime as dt

file = open('../secret.json')
API_KEYS = json.load(file)
SPOTIFY_CLIENT_ID = API_KEYS['Spotify_Client_ID']
SPOTIFY_CLIENT_SECRET = API_KEYS['Spotify_Client_Secret']
file.close()


class SpotifyTimeMachine:
    """
        This class creates a spotify time machine by scraping the billboard top 100 songs for a particular date
        and creating a spotify playlist with those songs and the spotipy api.
        Spotipy documentation api: https://spotipy.readthedocs.io/en/2.19.0/
    """

    def get_songs(self, date):
        """
        Get the top 100 song for the provided date
        :param date: The date in the format (yyyy-mm-dd) for the billboard top 100
        :return: list of songs in the format  [(song_name,artist_name),...]
        """
        top_100_url = "https://www.billboard.com/charts/hot-100/" + date.strip()
        response = requests.get(url=top_100_url)

        # Scrape the billboard chart and put the name of the top song and artist in a tuple list
        # in the format [(song_name,artist_name),...]
        soup = BeautifulSoup(response.text, "html.parser")
        song_soup = soup.find_all(class_="chart-element__information")
        songs = []
        print("Getting Songs from billboard top 100")
        for song in song_soup:
            song_name = song.find_next(class_="chart-element__information__song").getText()
            artist = song.find_next(class_="chart-element__information__artist").getText()
            songs.append((song_name, artist))
        return songs

    def get_song_uri(self, song, spotify):
        """
        Get the spotify uri for a given song by searching by the song name
        later we can try to add other search criteria
        :param spotify:
        :param song: tuple where the first item is the song's name
        :return: Spotify URI - The resource identifier that you can enter,
        for example, in the Spotify Desktop client’s search box to locate an artist, album, or track
        """
        uri_search_result = spotify.search(q=song[0], type='track')
        return uri_search_result["tracks"]["items"][0]["uri"]

    def make_spotify_playlist(self, songs, date):
        """
        using the list of songs in the format  [(song_name,artist_name),...] creates a spotify playlist
        :param date:
        :param songs: list of songs in the format  [(song_name,artist_name),...]
        :return:
        """

        credentials = SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                   client_secret=SPOTIFY_CLIENT_SECRET,
                                   redirect_uri="http://example.com",
                                   scope="playlist-modify-private")

        spotify = spotipy.Spotify(oauth_manager=credentials)

        new_playlist = spotify.user_playlist_create(name=f"{date} Billboard 100",
                                                    user=spotify.current_user()['id'],
                                                    public=False)
        # print(new_playlist)

        uri_list = []
        for song in songs:
            print("Getting URI for " + song[0])
            uri_list.append(self.get_song_uri(song, spotify))

        print("Adding Songs to Playlist")
        spotify.playlist_add_items(playlist_id=new_playlist['id'], items=uri_list)

    def run(self, date):
        """
         Entry point for the functionality of the SpotifyTimeMachine class
        :param date: The date in the format (yyyy-mm-dd)
        :return:
        """
        song_list = self.get_songs(date)
        time_machine.make_spotify_playlist(song_list, date)


if __name__ == '__main__':
    DEBUG = True
    date_to_use = input("Enter date in format (yyyy-mm-dd): ")
    # added the next line because I wanted a debug option that just uses the current date
    # Instead of random date like 2010-03-25
    date_to_use = date_to_use if date_to_use != "" and DEBUG else str(dt.date.today())
    print("Using " + date_to_use)
    time_machine = SpotifyTimeMachine()
    time_machine.run(date=date_to_use)
