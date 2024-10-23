from prompts import LYRICS_ANALYSIS_SONG_STYLE_PROMPT, LYRICS_ANALYSIS_INSTRUMENTS_PROMPT, TITLE_GENERATION_PROMPT, SONG_STYLE_GENERATION_PROMPT, LYRICS_GENERATION_PROMPT
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client = OpenAI()


def analyze_song_style(lyrics):
    """
    Analyzes the style of a song based on the lyrics.
    
    :param lyrics: The lyrics of the song to analyze.
    :return: A string describing the style of the song.
    """
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
    
    :param lyrics: The lyrics of the song to analyze.
    :return: A string describing the instruments of the song.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": LYRICS_ANALYSIS_INSTRUMENTS_PROMPT},
            {"role": "user", "content": f"Analyze these lyrics:\n\n{lyrics}"}
        ],
        max_tokens=500
    )
    return response.choices[0].message.content.strip()

def generate_song_title(title, lyrics, style, language, thought):
    """
    Generates a song title based on the title, lyrics, style, language, and thought.
    
    :param title: The original title of the song.
    :param lyrics: The lyrics of the song.
    :param style: The style of the song.
    :param language: The language of the song.
    :param thought: The songwriter's thought.
    :return: A string containing the generated song title.
    """
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
    
    :param song_style: The song style to analyze.
    :param thought: The songwriter's thought.
    :return: A string containing the generated song style.
    """
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