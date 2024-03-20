import spotipy
from spotipy.oauth2 import SpotifyOAuth


if __name__ == '__main__':
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                                                   client_secret='12345678901234567890',
                                                   redirect_uri='https://localhost:9999/callback'))

    song = input('What song would you like to search for? ')
    print(f'\nSearching Spotify for {song}...\n')

    search_results = sp.search(q=song, limit=5)

    result_num = 1
    artist_name = ''
    song_name = ''

    for track in search_results['tracks']['items']:
        song_name = track["name"]
        artist_name = track["artists"][0]["name"]
        release_date = track['album']['release_date']

        full_title = ' - '.join([artist_name, song_name])

        print(f'Result #{result_num}: {full_title: <75} \tReleased on {release_date}')
        result_num += 1
