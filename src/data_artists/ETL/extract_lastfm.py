lazy import requests
lazy import os
lazy from dotenv import load_dotenv

def getArtist(endpoint: str, API_KEY: str, artist_name: str) -> dict[str, int]:
    params = {
        "method" : "artist.getinfo",
        "artist" : artist_name,
        "api_key" : API_KEY,
        "format" : "json"
    }

    response = requests.get(endpoint, params=params).json()
    artist_info = response['artist']

    total_listeners = int(artist_info['stats']['listeners'])
    total_playcount = int(artist_info['stats']['playcount'])

    return {
        'total_listeners' : total_listeners,
        'total_playcount' : total_playcount
    }

if __name__ == "__main__":
    load_dotenv()
    API_KEY: str = os.getenv("LASTFM_API_KEY")
    endpoint: str = "https://ws.audioscrobbler.com/2.0/"
    getArtist(endpoint, API_KEY, "Hindia")
