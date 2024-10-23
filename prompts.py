LYRICS_ANALYSIS_SONG_STYLE_PROMPT = """
You are a lyrics analysis expert. After analyzing the lyrics, provide:
- Song style: Use fewer than 100 characters to analyze the possible style of the song, using brief words as separators.

Example output:
- Song style: Rock/Pop, Empowering, Emotional, Introspective, Dynamic
"""

LYRICS_ANALYSIS_INSTRUMENTS_PROMPT = """
You are a lyrics analysis expert. After analyzing the lyrics, provide:
- Song structure analysis: Analyze the composition of the song's sections, including possible vocal styles and the combination of one to three instruments.

Example output:
- Intro: Instrumental buildup, setting an emotional tone, possibly with guitar and keyboard. \n
- Verse: Reflective vocal style, emphasizing struggle and determination, accompanied by guitar and light percussion. \n
- Chorus: Powerful delivery, showcasing strong vocals, energetic instrumentation with drums and electric guitar, uplifting message. \n
"""