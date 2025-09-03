import os
from crewai.tools import tool
from crewai_tools import FileWriterTool, FileReadTool

# ✅ Built-in file tools
file_writer_tool = FileWriterTool()
file_reader_tool = FileReadTool()

# 🎙️ Custom Voice Tool (TTS) — using OpenAI example
from openai import OpenAI
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

    response = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=text
    )

    with open(filepath, "wb") as f:
        f.write(response.read())

    return f"🎧 Podcast audio saved to {filepath}"