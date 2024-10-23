import os
import requests
from requests.exceptions import Timeout, RequestException
from dotenv import load_dotenv

load_dotenv()


def generate_song(your_thought_input, generated_lyrics, style_input, title_input, instrumental_only=False):
    """
    Generate a song using the Suno API.

    :param your_thought_input: The user's thought input.
    :param generated_lyrics: The generated lyrics.
    :param style_input: The style input.
    :param title_input: The title input.
    :param instrumental_only: Whether to generate an instrumental only song.
    :return: A tuple containing the image URL and audio URL of the generated song.
    """  
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
