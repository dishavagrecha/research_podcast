# Research Paper → Podcast Generator

**From dense research papers to engaging podcasts in minutes.**  
This project automates the process of reading research papers, extracting insights, structuring them, writing a podcast script, and finally generating narrated audio.

---

## Overview

Academic research is often **complex and inaccessible**.  
This project uses **multi-agent AI (CrewAI + OpenAI)** to:

1. **Analyze** a research paper.
2. **Summarize** into structured notes (Problem, Methods, Results, Implications).
3. **Write** a snappy two-host podcast script.
4. **Narrate** the script into an **MP3 podcast** using AI voice synthesis.

> Example: Inputting _"Attention Is All You Need"_ PDF → Outputting a narrated podcast episode.

---

## Tech Stack

- **Python 3.11+**
- [CrewAI](https://github.com/joaomdmoura/crewai) – multi-agent orchestration
- [OpenAI GPT-4o](https://platform.openai.com/) – LLM + TTS (text-to-speech)
- **YAML** – for agent & task configuration
- **PyPDF2** – PDF text extraction
- **Telegram Bot API** _(optional)_ – deliver podcast directly to chat

---

## Project Structure

```
research_podcast/
│── config/
│   ├── agents.yaml         # Agent definitions
│   ├── tasks.yaml          # Task definitions
│── outputs/                # Generated reports, scripts, and MP3s
│── crew.py             # Crew orchestration
│── attention-is-all-you-need.pdf  # Sample paper
│── main.py                 # Entrypoint
│── README.md               # This file
```

---

## ⚡ Setup & Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/your-username/research_podcast.git
   cd research_podcast
   ```

2. **Create virtual environment**

   ```bash
   uv venv
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   uv pip install -r requirements.txt
   ```

4. **Set environment variables**  
   Create a `.env` file:
   ```env
   OPENAI_API_KEY=your_openai_key_here
   TELEGRAM_BOT_TOKEN=your_bot_token   # optional
   TELEGRAM_CHAT_ID=your_chat_id       # optional
   ```

---

## Usage

Run the pipeline:

```bash
uv run python main.py
```

Outputs:

- `outputs/report-<timestamp>.md` → Research notes
- `outputs/script-<timestamp>.md` → Podcast script
- `outputs/narration-<timestamp>.mp3` → Final podcast audio

---

## (Optional) Telegram Delivery

If configured, the final MP3 is sent to your Telegram chat automatically.  
Otherwise, find it in the `outputs/` folder.

---

## Demo Flow

1. Upload PDF → AI reads and extracts key insights.
2. Notes → converted into structured **report**.
3. Report → expanded into a **podcast script**.
4. Script → converted into **MP3 narration**.

---

## Impact

Reduced research paper reading time by ~70% for early testers.

---

## License

MIT License  
Free to use & modify.

---

_Turn research into podcasts, faster than ever._
