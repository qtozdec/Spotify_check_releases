from datetime import datetime, timedelta
import tekore as tk
from app.loader import bot
from app.config import ADMINS_ID

conf = tk.config_from_environment(return_refresh=True)
token = tk.refresh_user_token(*conf[:2], conf[3])
sp = tk.Spotify(token, max_limits_on=True, chunked_on=True)


async def test():
    id_artist_list = [artist.id for artist in sp.all_items(sp.followed_artists())]
    uri_songs_list = list()
    id_list = list()
    # id_list_add = list()
    song_list = list()
    now = (datetime.utcnow() + timedelta(hours=3)).strftime("%Y-%m-%d")
    # now = '2020-10-23'
    for artist in id_artist_list:  # Для каждого айди исполнителя из списка исполнителей
        albums = sp.artist_albums(artist)  # Находим все альбомы исполнителя
        for album in albums.items:
            if str(album.album_group) != 'appears_on' and album.release_date == now and album.id not in id_list:
                # для всех альбомов находим тот, который выпущен сегодня
                list_pesen = list()
                for k in album.artists:
                    list_pesen.append(k.name)
                stroka = ' & '.join(list_pesen) + ' - ' + album.name
                song_list.append(stroka)

                track_paging = sp.album_tracks(album.id)
                id_list.append(album.id)
                for item in track_paging.items:
                    uri_songs_list.append(item.uri)

    if uri_songs_list:
        check_playlist = [playlist.name for playlist in sp.followed_playlists().items]

        if not (check_playlist.count(now)):
            id_album = sp.playlist_create('om8u6cmy29znuq8xq9n0snlei', now, True).id
            sp.playlist_add(id_album, uri_songs_list)
            for k in song_list:
                await bot.send_message(ADMINS_ID[0], k)

