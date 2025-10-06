# 🎧 YouScribe

**Turn YouTube videos into clean, readable summaries.**

YouScribe is a simple yet powerful desktop app that fetches YouTube video transcripts, cleans them up, and converts them into short, well-structured articles you can actually read and understand.

Built with **Python** and **CustomTkinter**, YouScribe combines elegant design with the power of **Google Gemini** to make long videos instantly digestible.

---

## ✨ Features

* 🎬 **YouTube Transcription** – Paste any YouTube link and instantly fetch the full transcript.
* 🧠 **Smart Summarization** – Converts transcripts into concise, easy-to-read articles.
* 🌐 **Web Article Mode** – Works with normal websites too — just paste the link.
* 🖤 **Modern UI** – Dark mode interface with smooth typography and a minimal feel.
* ⚡ **One-Click Process** – Paste → Process → Read. That’s it.

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **CustomTkinter** – for the modern UI
* **YouTubeTranscriptApi** – for fetching video transcripts
* **Google Gemini API** – for AI summarization
* **requests**, **html2text**, **re** – for article and text processing

---

## 🚀 Installation

```bash
git clone https://github.com/<your-username>/YouScribe.git
cd YouScribe
pip install -r requirements.txt
python main.py
```

> 💡 *You’ll need a Google Gemini API key to use the summarization feature.*

---

## ⚙️ Usage

1. Launch the app.
2. Paste a YouTube link (or a normal webpage URL).
3. Click **Start Transcription**.
4. Read your generated summary right inside the app.

---

## ⚠️ Common Errors

### 🕒 1. App window shows “Not Responding”

This isn’t actually a bug — it usually happens while the AI is generating a detailed response for longer transcripts.
Just wait a bit; the app will display the output once Gemini finishes processing.

### 🔗 2. “YouTube URL not valid”

This means there’s an issue with the link you entered.
Make sure it’s a valid YouTube video URL (not a playlist, shorts page, or embed link) and try again.

### 🚫 3. “Error! Please check console for more details”

If the console mentions *“quota limit exceeded”*, it means your Google API key temporarily hit its request limit.
This usually lasts only for a few seconds — simply wait a short while and try again.

---

## 📸 UI Preview

<img width="866" height="652" alt="image" src="https://github.com/user-attachments/assets/78e3362d-e59d-46cc-848e-f78d3a227673" />


---

## 🧑‍💻 Author

**John Mathew**
Made with 💓 in India

---

## 📜 License

MIT License — free to use, modify, and share.

