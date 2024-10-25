# Suno Song Generation Agent

An Agent capable of querying song information, analyzing songs, and generating song details
Powered by [SwamZero Agent](https://github.com/swarmzero/swarmzero)

## Why I want to build this agent

The reason I want to build this app is because when we hear a song, I want to generate something similar to it.
However, as I'm not a professional musician, I don't know how the song is composed,
whether it's rock or jazz, or what instruments it's made up of.
So even when convenient tools like Suno appear, where you can generate songs just by providing prompts,
I still don't know how to do it effectively.

Through AI tools to help me analyze the composition of the song,
and generate prompts that can be used with Suno,
and then generate the song I want through Suno.
This is the purpose of this tool.

Through chat, you can interact with the agent to generate songs.
Through the SwamZero Agent, you can also interact with the agent to generate songs, 
including calling the corresponding tools to query song lyrics and other data,
analyzing song lyrics and Suno metatags to generate appropriate prompts.
Finally, generate the song you want through Suno.

## Features
 

## How to use 

### Register a Suno account
First, you need a Suno account. Register at [Suno](https://suno.ai/).

### Start the Suno API service
please refer to the [Suno API documentation](https://github.com/gcui-art/suno-api)
**Note**: You need to create a `.env` file at the root of the Suno API server and add the following environment variables:

```bash
SUNO_COOKIE=<your_suno_cookie>
```

[How to obtain the cookie of your Suno account](https://github.com/gcui-art/suno-api?tab=readme-ov-file#1-obtain-the-cookie-of-your-appsunoai-account)

**Note**: The default port for the Suno API server is 3000. If this port conflicts with other services, you can directly modify the docker-compose.yml file to change the port settings.
you need to specify a different port for the Suno API server, for example: `http://localhost:4000`

I recommend using docker to run the Suno API server.
Before running the docker, you need to change the `docker-compose.yml` file to specify a different port from the one used by the Langfuse server.

For example, change the `docker-compose.yml` file to:

```yaml
    ports:
      - "4000:3000"
```

Then, run the docker compose: 

```bash
docker compose build && docker compose up -d
```


### Enable Langtrace
Enable [Langtrace](https://www.langtrace.ai/), register for Langtrace , create a new project to obtain the key.

### Enable Musixmatch

We use Musixmatch to query song lyrics and other information.
Register at [Musixmatch](https://developer.musixmatch.com/), and get the API key.

### Setup .env file

create a `.env` file at the root of the project, and add the following environment variables:

```bash
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

Check the `swarmzero.yaml`, you can modify the model, environment, etc.

### Run the project

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python app.py
```

### Start the Frontend

## TODO
