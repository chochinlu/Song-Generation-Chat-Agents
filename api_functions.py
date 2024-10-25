import os
import requests
from requests.exceptions import Timeout, RequestException
from dotenv import load_dotenv
from pytubefix import YouTube

load_dotenv()

def check_suno_credits():
    """
    Check the Suno API credits.
    Only call this function when user mentions "suno credits" or "suno credit".
    
    :return: A dictionary containing the Suno API credits.
    """
    print("checking suno credits")
    try:
        response = requests.get(f"{os.getenv('SUNO_API_HOST')}/api/get_limit")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return f"Error checking Suno credits: {str(e)}"


def generate_song(your_thought_input, generated_lyrics, style_input, title_input, instrumental_only=False):
    """
    Generate a song using the Suno API.

    :param your_thought_input: The user's thought input.
    :param generated_lyrics: The generated lyrics.
    :param style_input: The style input.
    :param title_input: The title input.
    :param instrumental_only: Whether to generate an instrumental only song.
    :return: the image URL and audio URL of the generated song.  Audio urls within are wrapped in audio tags. One image is paired with one audio link.
    """  
    print("generating song")
    url = f"{os.getenv('SUNO_API_HOST')}/api/custom_generate"
    payload = {
        "prompt": generated_lyrics if not instrumental_only else your_thought_input,
        "title": title_input,
        "tags": style_input,
        "make_instrumental": instrumental_only,
        "wait_audio": True,
    }
    
    timeout = 600  # 10 minutes
    try:
        response = requests.post(url, json=payload, timeout=timeout)
        response.raise_for_status()
        result = response.json()
        print("result: ", result)
        
        outputs = []
        for song in result[:2]:
            outputs.extend([song.get('image_url', ''), song['audio_url']])
        
        while len(outputs) < 4:
            outputs.extend([None, None])
        
        return outputs
    except Timeout:
        error_message = f"Request timed out after {timeout} seconds. Please try again later."
        return error_message
    except RequestException as e:
        error_message = f"Error generating song: {str(e)}"
        return error_message
    except Exception as e:
        error_message = f"Unexpected error: {str(e)}"
        return error_message

def get_youtube_title(youtube_url):
    """
    Get the title of a YouTube video.
    This function is called when the user only inputs a YouTube URL to retrieve the title of the YouTube video
    
    :param youtube_url: The URL of the YouTube video.
    :return: A string containing the YouTube video title.
    """
    print("getting youtube title")
    yt = YouTube(youtube_url)
    
    return yt.title

def get_lyrics(track_name, artist_name):
    """
    Get the lyrics of a song by its name and artist.
    This function is called when there's a song name and artist to retrieve the lyrics of the song
    Always call the Musixmatch API to retrieve lyrics
    
    :param track_name: The name of the song.
    :param artist_name: The name of the artist.
    :return: A string containing the lyrics of the song.
    """
    print("getting lyrics by using musixmatch api")
    base_url = 'https://api.musixmatch.com/ws/1.1/track.search'
    params = {
        'apikey': os.getenv('MUSIXMATCH_API_KEY'),
        'q_track': track_name,
        'q_artist': artist_name,
        'page_size': 1,
        's_track_rating': 'desc'
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if data['message']['header']['status_code'] == 200:
        track_list = data['message']['body']['track_list']
        if track_list:
            track_id = track_list[0]['track']['track_id']
            return get_lyrics_by_track_id(track_id)
    return None

def get_lyrics_by_track_id(track_id):
    """
    Get the lyrics of a song by its track ID.
    Always call the Musixmatch API to retrieve lyrics
    :param track_id: The ID of the song.
    :return: A string containing the lyrics of the song. 
    """
    print("getting lyrics by using musixmatch api and track id")
    lyrics_url = f'https://api.musixmatch.com/ws/1.1/track.lyrics.get?apikey={os.getenv('MUSIXMATCH_API_KEY')}&track_id={track_id}'
    response = requests.get(lyrics_url)
    data = response.json()
    
    if data['message']['header']['status_code'] == 200:
        return data['message']['body']['lyrics']['lyrics_body']
    return None

def get_youtube_video_url(query:str):
    """
    Get the video URL of a YouTube video.

    :param query: The query to search for on YouTube.
    :return: A list containing the URL of the YouTube video.
    """
    print("getting youtube video url")
    youtube_api_key = os.getenv('YOUTUBE_API_KEY')
    MAX_RESULTS = 3
    youtube_search_url = f'https://www.googleapis.com/youtube/v3/search?key={youtube_api_key}&q={query}&type=video&maxResults={MAX_RESULTS}&key={youtube_api_key}'
    response = requests.get(youtube_search_url)
    data = response.json()
    video_urls = []
    for item in data['items']:
        video_urls.append(f"https://www.youtube.com/watch?v={item['id']['videoId']}")
    return video_urls

def serp_search(query:str, language:str="en"):
    """
    Search the web for a query using the Serp API

    :param query: The query to search for on the web.
    :param language: The language to search for on the web.
    
    :return: a dictionary containing the search results
    """
    print("searching the web for a query using the Serp API")
    serp_api_key = os.getenv('SERP_API_KEY')
    serp_search_url = f'https://serpapi.com/search.json?q={query}&hl={language}&api_key={serp_api_key}&google_domain=google.com'
    response = requests.get(serp_search_url)
    data = response.json()
    return data
