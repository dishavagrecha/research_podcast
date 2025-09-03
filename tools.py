import os
from crewai.tools import tool
from crewai_tools import FileReadTool
from openai import OpenAI

file_reader_tool = FileReadTool()

# 🎙️ OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@tool("voice_tool")
def voice_tool(text: str, filename: str = "podcast.mp3") -> str:
    """
    Converts text to speech and saves it as an MP3 file.
    Args:
        text (str): Podcast script text.
        filename (str): Output audio filename.
    Returns:
        str: Confirmation with saved path.
    """
    os.makedirs("outputs", exist_ok=True)
    filepath = os.path.join("outputs", filename)

    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=text,
    ) as response:
        response.stream_to_file(filepath)

    return f"Podcast audio saved to {filepath}"
