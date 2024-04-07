import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Initialisation de l'API Spotify avec les identifiants d'application
client_credentials_manager = SpotifyClientCredentials(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def recherche_chansons_par_bpm(bpm_min, bpm_max):
    # Recherche de chansons avec le BPM dans la plage spécifiée
    tracks = sp.search(q='tempo:{}-{}'.format(bpm_min, bpm_max), type='track', limit=50)
    return tracks['tracks']['items']

def classement_par_genre(chansons):
    genres = {}
    for chanson in chansons:
        for genre in chanson['track']['genres']:
            if genre in genres:
                genres[genre].append(chanson)
            else:
                genres[genre] = [chanson]
    return genres

def creer_playlist(chansons):
    # Création d'une nouvelle playlist sur Spotify
    playlist_name = "Playlist automatique"
    playlist = sp.user_playlist_create(user='YOUR_USERNAME', name=playlist_name)
    
    # Ajout des chansons à la playlist
    track_uris = [chanson['track']['uri'] for chanson in chansons]
    sp.user_playlist_add_tracks(user='YOUR_USERNAME', playlist_id=playlist['id'], tracks=track_uris)

# Exemple d'utilisation
bpm_min = 50
bpm_max = 200
chansons = recherche_chansons_par_bpm(bpm_min, bpm_max)
genres_classe = classement_par_genre(chansons)
# Sélection d'un genre spécifique (par exemple, rock)
chansons_rock = genres_classe.get('rock', [])
creer_playlist(chansons_rock)
