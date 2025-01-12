import customtkinter
from webscout import YTTranscriber
import google.generativeai as genai
import os
genai.configure(api_key='AIzaSyAAufJESqqpF6HT4-zdMiTyS4f2Rvq6yJE')
model = genai.GenerativeModel("gemini-1.5-flash")
def chat(text):
    response = model.generate_content(text)
    return response.text
yt = YTTranscriber()
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

def transcribe(video_url):
    transcript = yt.get_transcript(video_url, languages=None) 
    text=""
    for i in transcript:
        text+=" "+f"{i['text']}"
    print(text)
    R = chat(f"Convert this video transcript into a readable article, explaining every single thing in the transcript. It must be understandable in detail, it must cover everything in detail. Transcript -  {text}")
    return R
app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("1920x1080")
I=customtkinter.CTkLabel(app,text="Youtube Transcriber $ Summariser",justify="left")
I.configure(font=("Segoe UI Variable Small Semibold",65))
I.pack()
J=customtkinter.CTkLabel(app,text="\n\n")
J.configure(font=("Segoe UI Variable Small Semibold",20))
J.pack()
entry = customtkinter.CTkEntry(app, placeholder_text="Youtube Link")
entry.pack()
def button_function():
    global text
    link=entry.get()
    text=transcribe(link)
    print(text)
    axt=customtkinter.CTkTextbox(master=app, width=400)
    axt.insert("0.0",text)
    axt.pack()

K=customtkinter.CTkLabel(app,text="\n\n")
K.configure(font=("Segoe UI Variable Small Semibold",20))
K.pack()
# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="Continue", command=button_function)
button.pack()
app.mainloop()
