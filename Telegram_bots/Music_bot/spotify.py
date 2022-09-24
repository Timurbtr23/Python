from pprint import pprint

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="6471c45cc1c94b1abd37d09fe11c0c79",
                                                           client_secret="6f7189d1a4f54dc992e8a249455a6eec"))


def get_album_tracks(url):
    results = sp.album_tracks(album_id=url)
    for track in results['items']:
        artist = track['artists'][0]['name']
        print(artist, track['name'])


def get_playlist_tracks(url):
    results = sp.playlist_tracks(playlist_id=url)
    for track in results['items']:
        artist = track['track']['album']['artists'][0]['name'] + " "
        title = track['track']['name']
        print(artist + title)


def get_track_id(search_data):
    results = sp.search(q=search_data, type='track', limit=5)

    for track in results["tracks"]["items"]:
        name = track['album']['name']
        artist = track['album']['artists'][0]['name']
        print(artist, name)
        print(track['album'])
        print("??????????????????????????????????????????")
    # if results['artists']['total'] == 0:
    #     return 'error'
    # else:
    #     return results['artists']['items'][0]['id']


def get_artist_id(search_data):
    results = sp.search(q=search_data, type="artist", limit=5)

    if results['artists']['total'] == 0:
        return 'error'
    else:
        return results['artists']['items'][0]['id']


def get_similar_artists(search_data):
    id = get_artist_id(search_data)

    if id == 'error':
        print("Не найдено")
        return

    results = sp.artist_related_artists(id)

    for count, artist in enumerate(results['artists']):
        print(count+1, artist['name'])


data = input()
get_track_id(data)

# https://open.spotify.com/playlist/5Pxn5vrNaz6TuD7itqPmF6?si=10371875bd4b45d7&pt=462385a953d122e2432f06242b1650bb
# https://open.spotify.com/playlist/37i9dQZF1E3601AlRn4A2y?si=63f1edfadb2f4181
# https://open.spotify.com/album/2K3wJ4mPSekES5SPth484n?si=wvpR9RDlR2WzSwPgIRO80w
