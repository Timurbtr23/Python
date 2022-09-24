import lyricsgenius
import api_key

LyricsGenius = lyricsgenius.Genius(api_key.client_access_token)


def find_lyrics(input_data: str):
    song = LyricsGenius.search_song(input_data)
    return song.lyrics


def find_song_by_lyrics(input_data: str):
    song = LyricsGenius.search_song(input_data)
    song_info = song.artist + " - " + song.title
    return song_info


info_text = "Введите название песни и исполнителя: "
print(find_song_by_lyrics(input(info_text)))
# print(find_lyrics(input(info_text)))
