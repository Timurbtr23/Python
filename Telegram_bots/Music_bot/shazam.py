import asyncio
from shazamio import Shazam, Serialize
from pprint import pprint


async def recognize_by_file(file):
    # Todo Картинку песенки добавить
    shazam = Shazam()
    out = await shazam.recognize_song(file)
    name = out['track']['title']
    artist = out['track']['subtitle']
    print(artist + " - " + name)


async def search_for_track(search_info):
    #  Пользователь выбирает один из предложенных треков и получит айди. Этот айди суём в similar_tracks()
    shazam = Shazam()
    tracks = await shazam.search_track(query=search_info, limit=5)
    list = {}
    if tracks:
        count_of_finded_songs = len(tracks['tracks']['hits'])
        for i in range(count_of_finded_songs):
            info = tracks['tracks']['hits'][i]['heading']
            id = int(tracks['tracks']['hits'][i]['actions'][0]['id'])
            list[info['subtitle'] + " - " + info['title']] = id
        pprint(list)
    else:
        print("Не найдено")


async def similar_tracks(track_id):
    shazam = Shazam()
    related = await shazam.related_tracks(track_id=track_id, limit=10)
    tracks = []
    for i in range(10):
        tracks.append(related['tracks'][i]['subtitle'] + " - " + related['tracks'][i]['title'])
    pprint(tracks)


file = '/home/timurbtr23/Downloads/My recording 1.mp3'

loop = asyncio.get_event_loop()
loop.run_until_complete(recognize_by_file(file))
print()
loop.run_until_complete(search_for_track("Кизару Narcos"))
print()
loop.run_until_complete(similar_tracks(531478837))
