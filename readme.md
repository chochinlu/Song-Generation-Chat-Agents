# Suno Song Generation Agent

An Agent capable of querying song information, analyzing songs, and generating song details
Powered by [SwamZero Agent](https://github.com/swarmzero/swarmzero)

## Why I want to build this agent

When we hear a song we like, we might want to create similar music. However, for non-professional musicians, this is often challenging because:

1. We may not understand the specific composition of the song.
2. We might be unable to identify the song's style (e.g., rock or jazz).
3. We may not know which instruments are used in the song.

Even with convenient tools like Suno, where songs can be generated just by providing prompts, we might still not know how to use them effectively.

## Purpose of this application

This tool aims to address the above issues, primarily through:

1. Using AI tools to analyze the composition of songs.
2. Generating prompts suitable for use with Suno.
3. Creating the songs we want through Suno.

## Features

1. Main Chat Interface
   - Powered by SwarmZero AI agent
   - Integrates Google search, YouTube search, and Musixmatch search
   - Allows users to search for any song-related items (songs, artists, albums, lyrics, etc.)
   - Specially supports YouTube video search, with results including directly clickable video URLs and summaries

2. Song Analysis
   - Combines lyrics, search results, Suno's suggested metatags, and song classification categories
   - Analyzes song styles and structures

3. Music Knowledge Base
   - Allows users to freely search and play songs
   - Helps understand song styles and structures

4. Suno Song Generation
   - Combines user ideas with analyzed song styles and structures
   - Generates new Suno song prompts
   - Creates Suno songs
   - Provides song cover preview and playback functionality

5. Suno Status Check
   - Users can check the current available status of Suno

6. Sidebar Functionality
   - Provides various prompt shortcuts
   - Top-to-bottom flow represents a complete song generation process
   - Each prompt also functions as an individual tool that can be called separately
   - Provides clear instructions when the Agent encounters difficulties

## Usage Flow

1. Use the chat interface to search for and analyze songs
2. Utilize the music knowledge base to understand song styles and structures
3. Combine personal ideas to generate Suno song prompts
4. Use Suno to generate songs
5. Preview and play the generated songs

Note: Throughout the process, the sidebar provides convenient prompts and tools to help users complete each step.

## How to use 

### Prerequisites

1. Register a Suno account
   - Sign up at [Suno](https://suno.ai/)

2. Start the Suno API service
   - The Suno API is used for creating and viewing Suno songs
   - It provides functionality for generating new songs and retrieving the status of generated songs
   - This API serves as a crucial interface for interacting with the Suno platform, allowing us to programmatically utilize Suno's AI music generation capabilities
   - Refer to the [Suno API documentation](https://github.com/gcui-art/suno-api)
   - Create a `.env` file at the root of the Suno API server and add:
     ```
     SUNO_COOKIE=<your_suno_cookie>
     ```
   - How to obtain your Suno cookie: [Instructions](https://github.com/gcui-art/suno-api?tab=readme-ov-file#1-obtain-the-cookie-of-your-appsunoai-account)
   - **Note**: The default port for the Suno API server is 3000. If this port conflicts with other services, you can modify the `docker-compose.yml` file to change the port settings.
   - To use a different port (e.g., 4000), modify the `docker-compose.yml` file:
     ```yaml
     ports:
       - "4000:3000"
     ```
   - Run the Docker Compose:
     ```bash
     docker compose build && docker compose up -d
     ```
   - Specify the new port in your configuration: `http://localhost:4000`

3. Enable Langtrace
   - Langtrace is used to monitor the status and performance of SwarmZero Agent
   - It provides detailed tracking and analysis capabilities to help developers understand the Agent's operation
   - Through Langtrace, you can view the Agent's conversation flow, decision-making process, and resource usage
   - Register at [Langtrace](https://www.langtrace.ai/)
   - Create a new project and obtain the API key

4. Enable Musixmatch
   - Musixmatch is used to search for song lyrics
   - Register at [Musixmatch](https://developer.musixmatch.com/) and obtain the API key

5. Enable Google YouTube API
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one
   - Search for and enable "YouTube Data API v3" in the API Library
   - Create an API key in the Credentials page
   - Copy the API key for later use

6. Enable SerpAPI
   - SerpAPI is used to obtain Google search results
   - It provides a simple way to access Google search results without directly dealing with the complex Google Search API
   - Through SerpAPI, we can easily retrieve various types of search data including web search results, images, news, and more
   - This is particularly useful for our project, as it can be used to collect music-related information, artist backgrounds, and other relevant data
   - Register for a [SerpAPI](https://serpapi.com/) account
   - Obtain the API key


### Environment Setup

1. Create and configure the `.env` file at the root of the project
   ```
   MODEL=<your_model>
   ENVIRONMENT=dev
   OPENAI_API_KEY=<your_openai_api_key>
   MISTRAL_API_KEY=<your_mistral_api_key>
   ANTHROPIC_API_KEY=<your_anthropic_api_key>
   SWARMZERO_LOG_LEVEL=INFO
   SWARMZERO_DATABASE_URL=
   PINECONE_API_KEY=
   AWS_ACCESS_KEY_ID=
   AWS_SECRET_ACCESS_KEY=
   LANGTRACE_API_KEY=<your_langtrace_api_key>
   SUNO_API_HOST=<your_suno_api_host>
   MUSIXMATCH_API_KEY=<your_musixmatch_api_key>
   ```

2. Check and modify the `swarmzero.yaml` file as needed

### Starting the Service

1. Install dependencies
   ```
   pip install -r requirements.txt
   ```

2. Run the project
   ```
   python app.py
   ```

5. Start the frontend (specific steps to be added)

## Screenshots
