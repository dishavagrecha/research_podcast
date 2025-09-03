from datetime import datetime
import glob
import os
import warnings
from crew import ResearchCrew
from dotenv import load_dotenv

from telegram import send_telegram_file, send_telegram_message

load_dotenv()

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs',
        'current_month': str(datetime.now().month),
        'current_year': str(datetime.now().year)
    }
    
    try:
        ResearchCrew().crew().kickoff(inputs=inputs)
        send_telegram_message("🎙️ Podcast Script Generated!")
        
        # ✅ Send generated files (if you want)
        mp3_files = glob.glob("outputs/*.mp3")
        if mp3_files:
            latest_mp3 = max(mp3_files, key=os.path.getctime)
            send_telegram_file(latest_mp3, caption="Here’s your podcast audio 🎙️")
        else:
            send_telegram_message("⚠️ No MP3 file found in outputs folder.")


    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if __name__ == "__main__":
    run()