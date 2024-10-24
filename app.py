import asyncio
from swarmzero.sdk_context import SDKContext
from swarmzero import Agent
from dotenv import load_dotenv
from ai_functions import (
    analyze_song_style,
    analyze_song_instruments,
    generate_song_title,
    generate_song_style,
    generate_lyrics,
    get_youtube_title,
    get_youtube_song_name_and_artist,
    get_lyrics,
)
from api_functions import generate_song, check_suno_credits

load_dotenv()

sdk_context = SDKContext(config_path="./swarmzero_config.toml")

song_generator_agent = Agent(
    name="song_generator_agent",
    functions=[
        analyze_song_style, 
        analyze_song_instruments, 
        generate_song_title, 
        generate_song_style, 
        generate_lyrics,
        generate_song,
        check_suno_credits,
        get_youtube_title,
        get_youtube_song_name_and_artist,
        get_lyrics,
    ],
    instruction="A song generator agent that analyzes a song and generates prompts for a song generator model.",
    sdk_context=sdk_context,
    # chat_only_mode=True,
)

if __name__ == "__main__":
    song_generator_agent.run()
    # asyncio.run(song_generator_agent.chat("Generate a song about ..."))
