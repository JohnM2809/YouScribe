import customtkinter
from webscout import YTTranscriber
import requests
import html2text
import re
import google.generativeai as genai
import os
genai.configure(api_key='AIzaSyAAufJESqqpF6HT4-zdMiTyS4f2Rvq6yJE')
model = genai.GenerativeModel("gemini-1.5-flash")
def chat(text):
    response = model.generate_content(text)
    return response.text
def url_to_plain_text(url):

    response = requests.get(url)

    response.raise_for_status()  # Raise an exception if the request fails

    text_maker = html2text.HTML2Text()

    plain_text = text_maker.handle(response.text)

    return plain_text
web_link = "https://www.example.com"



yt = YTTranscriber()
import google.generativeai as genai
genai.configure(api_key='AIzaSyAAufJESqqpF6HT4-zdMiTyS4f2Rvq6yJE')
model = genai.GenerativeModel("gemini-1.5-flash")
def chat(text):
    response = model.generate_content(text)
    return response.text

# Appearance settings
customtkinter.set_appearance_mode("Dark")  # Modes: System, Light, Dark
customtkinter.set_default_color_theme("green")  # Themes: blue, dark-blue, green
def youtube_parser(url):
    reg_exp = r'^.*((youtu\.be/)|(v/)|(u/\w/)|(embed/)|(watch\?))\??v?=?([^#&?]*).*'
    match = re.match(reg_exp, url)
    return match[7] if match and len(match[7]) == 11 else False
# Function to transcribe and summarize the video
def transcribe(video1_url):
    
    if "youtube.com" in video1_url or "youtu.be" in video1_url:
        video_url=f"https://www.youtube.com/watch?v={youtube_parser(video1_url)}"
        transcript = yt.get_transcript(video_url, languages=None) 
        text = ""
        for i in transcript:
            text += " " + f"{i['text']}"
        print(text)
        R = chat(f"Convert this video transcript into a readable article, explaining every single thing in the transcript. It must be understandable in detail, it must cover everything in detail. Transcript -  {text}")
        return R
    elif '.com' not in video_url:return "Please enter a video or article url."
    else:
        text=url_to_plain_text(video1_url)
        R=chat(f"Summarise this text or article. There may be useless hyperlinks and all, but ignore those. {text} ")
        return R

# Create the main app window
app = customtkinter.CTk()
app.geometry("866x650")  # Smaller, more manageable size
app.title("YouTube Transcriber & Summarizer")

# Title Label
title_label = customtkinter.CTkLabel(app, text="YouTube Transcriber & Summarizer", justify="center")
title_label.configure(font=("Segoe UI Variable Display", 40, "bold"))
title_label.pack(pady=20)  # Add spacing around the title

# Subtitle Label
subtitle_label = customtkinter.CTkLabel(app, text="Enter the YouTube link below to get started:", justify="center")
subtitle_label.configure(font=("Segoe UI Variable", 18))
subtitle_label.pack(pady=10)

# Entry Box for YouTube Link
entry = customtkinter.CTkEntry(app, placeholder_text="Paste YouTube Link Here", width=600)
entry.configure(font=("Segoe UI Variable", 16))
entry.pack(pady=10)

# Function for the button
def button_function():
    global text
    link = entry.get()
    if not link.strip():
        result_label.configure(text="Error: Please enter a valid YouTube link!", text_color="red")
        return
    result_label.configure(text="Processing...", text_color="orange")
    text = transcribe(link)
    result_label.configure(text="Transcription Complete!", text_color="green")
    # Display the result in a scrollable textbox
    result_textbox.delete("0.0", "end")
    result_textbox.insert("0.0", text)

# Button to start the process
button = customtkinter.CTkButton(app, text="Start Transcription", command=button_function, width=200, height=50)
button.configure(font=("Segoe UI Variable", 16, "bold"))
button.pack(pady=20)

# Label for status updates
result_label = customtkinter.CTkLabel(app, text="", justify="center")
result_label.configure(font=("Segoe UI Variable", 16))
result_label.pack(pady=10)

# Textbox for displaying results (scrollable)
result_textbox = customtkinter.CTkTextbox(app, width=700, height=300)
result_textbox.configure(font=("Consolas", 14), wrap="word")
result_textbox.pack(pady=10)
subtitle_label = customtkinter.CTkLabel(app, text="Made with 💓 by John", justify="center")
subtitle_label.configure(font=("Segoe UI Variable", 18))
subtitle_label.pack(pady=10)

# Run the application
app.mainloop()
