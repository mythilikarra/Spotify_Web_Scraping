import spotipy
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data
client_id = "8251b20d546e4e79b8db7a4fe4e29d6c"
client_secret = "47bd57fe65074305bbad8aea77a33b55"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API
name = "BTS" #chosen artist
result = sp.search(name) #search query
#print (result['tracks']['items'][0]['artists'])

#Extract Artist's uri
artist_uri = result['tracks']['items'][0]['artists'][0]['uri']
#Pull all of the artist's albums
sp_albums = sp.artist_albums(artist_uri, album_type='album')
#Store artist's albums' names' and uris in separate lists
album_names = []
album_uris = []
for i in range(len(sp_albums['items'])):
    album_names.append(sp_albums['items'][i]['name'])
    album_uris.append(sp_albums['items'][i]['uri'])
    
album_names
album_uris
#Keep names and uris in same order to keep track of duplicate albums
print (album_names)

#Extract key album track data
def albumSongs(uri):
	album = uri #assign album uri to a_name
	spotify_albums = {}	#Define spotify_albums
	spotify_albums[album] = {} #Creates dictionary for that specific album
	#Create keys-values of empty lists inside nested dictionary for album
	spotify_albums[album]["album"] = [] #create empty list
	spotify_albums[album]['track_number'] = []
	spotify_albums[album]['id'] = []
	spotify_albums[album]['name'] = []
	spotify_albums[album]['uri'] = []
	tracks = sp.album_tracks(album) #pull data on album tracks
	for n in range(len(tracks['items'])): #for each song track
        	spotify_albums[album]['album'].append(album_names[album_count]) #append album name tracked via album_count
        	spotify_albums[album]['track_number'].append(tracks['items'][n]['track_number'])
        	spotify_albums[album]['id'].append(tracks['items'][n]['id'])
        	spotify_albums[album]['name'].append(tracks['items'][n]['name'])
        	spotify_albums[album]['uri'].append(tracks['items'][n]['uri'])

#Get all albums

spotify_albums = {}

album_count = 0
for i in album_uris: #each album
    albumSongs(i)
    print("Album " + str(album_names[album_count]) + " songs has been added to spotify_albums dictionary")
    album_count+=1 #Updates album count once all tracks have been added

#Store audio features
def audio_features(album):
    #Add new key-values to store audio features
    spotify_albums[album]['acousticness'] = []
    spotify_albums[album]['danceability'] = []
    spotify_albums[album]['energy'] = []
    spotify_albums[album]['instrumentalness'] = []
    spotify_albums[album]['liveness'] = []
    spotify_albums[album]['loudness'] = []
    spotify_albums[album]['speechiness'] = []
    spotify_albums[album]['tempo'] = []
    spotify_albums[album]['valence'] = []
    spotify_albums[album]['popularity'] = []
    #create a track counter
    track_count = 0
    for track in spotify_albums[album]['uri']:
        #pull audio features per track
        features = sp.audio_features(track)
        
        #Append to relevant key-value
        spotify_albums[album]['acousticness'].append(features[0]['acousticness'])
        spotify_albums[album]['danceability'].append(features[0]['danceability'])
        spotify_albums[album]['energy'].append(features[0]['energy'])
        spotify_albums[album]['instrumentalness'].append(features[0]['instrumentalness'])
        spotify_albums[album]['liveness'].append(features[0]['liveness'])
        spotify_albums[album]['loudness'].append(features[0]['loudness'])
        spotify_albums[album]['speechiness'].append(features[0]['speechiness'])
        spotify_albums[album]['tempo'].append(features[0]['tempo'])
        spotify_albums[album]['valence'].append(features[0]['valence'])
        #popularity is stored elsewhere
        pop = sp.track(track)
        spotify_albums[album]['popularity'].append(pop['popularity'])
        track_count+=1    

#NEXT
