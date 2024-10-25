from prompts import LYRICS_ANALYSIS_SONG_STYLE_PROMPT, LYRICS_ANALYSIS_INSTRUMENTS_PROMPT, TITLE_GENERATION_PROMPT, SONG_STYLE_GENERATION_PROMPT, LYRICS_GENERATION_PROMPT
from dotenv import load_dotenv
from openai import OpenAI
import requests
import os
load_dotenv()

client = OpenAI()

def get_youtube_song_name_and_artist(youtube_title):
    """
    Get the song name and artist of a YouTube video.
    This function is called when there's a YouTube video title to retrieve the song name and artist information
    
    :param youtube_title: The title of the YouTube video.
    :return: A tuple containing the song name and artist.
    """
    print("getting youtube song name and artist")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a music expert who can analyze a YouTube video title and extract the song name and artist."},
            {"role": "user", "content": f"Analyze this YouTube video title:\n\n{youtube_title}\n\nExtract the song name and artist from the title."}
        ],
        max_tokens=500
    )
    return response.choices[0].message.content.strip()

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


def analyze_song_style(lyrics):
    """
    Analyzes the style of a song based on the lyrics.
    User can call this function when there's lyrics to analyze the song style
    Lyrics is from context of the song or user's input
    
    :param lyrics: The lyrics of the song to analyze.
    :return: A string describing the style of the song.
    """
    print("analyzing song style")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": LYRICS_ANALYSIS_SONG_STYLE_PROMPT},
            {"role": "user", "content": f"Analyze these lyrics:\n\n{lyrics}"}
        ],
        max_tokens=100
    )
    return response.choices[0].message.content.strip()

def analyze_song_instruments(lyrics):
    """
    Analyzes the instruments of a song based on the lyrics.
    User can call this function when there's lyrics to analyze the song instruments
    Lyrics is from context of the song or user's input
    
    :param lyrics: The lyrics of the song to analyze.
    :return: A string describing the instruments of the song.
    """
    print("analyzing song instruments")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": LYRICS_ANALYSIS_INSTRUMENTS_PROMPT},
            {"role": "user", "content": f"Analyze these lyrics:\n\n{lyrics}"}
        ],
        max_tokens=500
    )
    return response.choices[0].message.content.strip()

def generate_song_title(title, lyrics, style, language="en", thought=""):
    """
    Generates a song title based on the title, lyrics, style, language, and thought.
    User can call this function when there's a song title, lyrics, style, language, and thought to generate a song title
    
    :param title: The original title of the song.
    :param lyrics: The lyrics of the song.
    :param style: The style of the song.
    :param language: The language of the song.
    :param thought: The songwriter's thought.
    :return: A string containing the generated song title.
    """
    print("generating song title")
    prompt = TITLE_GENERATION_PROMPT.format(
        title=title,
        lyrics=lyrics,
        style=style,
        language=language,
        thought=thought
    )
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a creative songwriter specializing in crafting catchy song titles in multiple languages."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=30,
        temperature=0.5
    )
    
    generated_title = response.choices[0].message.content.strip()
    # Remove possible quotation marks and parentheses at the beginning or end of the title
    generated_title = generated_title.strip('"\'()[]{}')
    
    return generated_title

def generate_song_style(song_style, thought=""):
    """
    Generates a song style based on the song style and thought.
    This is a must to generate, it's prepared to provide to Suno API to generate a song
    
    :param song_style: The song style to analyze.
    :param thought: The songwriter's thought.

    :return: A string containing the generated song style.
    """
    print("generating song style")
    prompt = SONG_STYLE_GENERATION_PROMPT.format(
        style=song_style,
        thought=thought,
    )
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a creative music style generator."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=60,
        temperature=0.7
    )
    
    generated_style = response.choices[0].message.content.strip()
    return generated_style

def generate_lyrics(instruments, language, thought):
    """
    Generates lyrics based on the instruments, language, and thought.
    
    :param instruments: The instruments of the song.
    :param language: The language of the song.
    :param thought: The songwriter's thought.
    :return: A string containing the generated lyrics.
    """
    print("generating lyrics")
    prompt = LYRICS_GENERATION_PROMPT.format(
        instruments=instruments,
        language=language,
        thought=thought
    )
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a talented songwriter capable of creating lyrics in multiple languages."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    
    generated_lyrics = response.choices[0].message.content.strip()
    return generated_lyrics
