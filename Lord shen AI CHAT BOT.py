import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import speech_recognition as sr
import pyttsx3
import random
import threading
import webbrowser

#  jokes list and initial setup remain unchanged
jokes = [
    "Why don't scientists trust atoms? Because they make up everything.",
    "I told my wife she should embrace her mistakes. She gave me a hug.",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "I used to play piano by ear, but now I use my hands.",
    "Why can’t you give Elsa a balloon? Because she will let it go.",
    "What do you call fake spaghetti? An impasta!",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
    "How is called the chemical structure of magnesium and oxygen? oh my god! "
]

class VoiceAssistantGUI:
    def __init__(self, master):
        self.master = master
        master.title("Lord Shen AI CHAT BOT")

        # Text area
        self.text_area = ScrolledText(master, height=15, width=60)
        self.text_area.pack(padx=10, pady=10)

        # Speak button
        self.speak_button = tk.Button(master, text="Speak", command=self.start_listening)
        self.speak_button.pack(pady=5)

        # Initialize the TTS engine
        self.converter = pyttsx3.init()
        self.converter.setProperty('rate', 150)
        self.converter.setProperty('volume', 0.7)

    def speak(self, audio_string):
        self.converter.say(audio_string)
        self.converter.runAndWait()

    def start_listening(self):
        # Run the listening process in a non-blocking way
        threading.Thread(target=self.listen_and_respond, daemon=True).start()

    def listen_and_respond(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.text_area.insert(tk.END, "Listening...\n")
            audio_text = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio_text)
                self.text_area.insert(tk.END, "You: " + text + "\n")

                # Your existing conditions and responses
                if "hello" in text.lower():
                    self.speak("Hello there! How can I assist you today?")
                elif "good morning" in text.lower():
                    self.speak("Good morning! I hope you have a splendid day ahead. How can I help you?")
                elif "goodbye" in text.lower() or "bye" in text.lower():
                    self.speak("Goodbye! Don't hesitate to return if you need more assistance.")
                    root.destroy()

                    # Queries about the bot
                elif "what is your name" in text.lower():
                    self.speak("My name is Lord Shen, I am an AI chatbot at your service.")
                elif "who created you" in text.lower():
                    self.speak(
                        "I was created by a fifteen years old kid in greece"
                    )
                elif "help" in text.lower():
                    self.speak("Of course, I'm here to help you with everything you need.")
                elif "what is" in text.lower():
                    a = text.split()
                    try:
                        x = a.index("a")
                    except ValueError:
                        try:
                            x = a.index("an")
                        except ValueError:
                            x = a.index("is")
                    url_key_word = a[x+1:]
                    url_key_word = "".join(url_key_word)
                    print(url_key_word)
                    webbrowser.open_new("https://en.wikipedia.org/wiki/"+url_key_word)
                    self.speak(
                        f"you can find more about {url_key_word.title()} here!"
                    )
                elif "open" in text:
                    a = text.split()
                    x = a.index("open")
                    url_key_word = a[x+1:]
                    url_key_word = "".join(url_key_word)
                    webbrowser.open_new("https://www.google.com/search?client=firefox-b-d&q="+url_key_word)
                    self.speak(f"Here is {url_key_word}!!......... just click and you are in!")
                    # Fun or miscellaneous responses
                elif "tell me a joke" in text.lower():
                    choice = random.choice(jokes)
                    a = jokes.index(choice)
                    self.speak(choice)
                    jokes.pop(int(a))
                elif "do" in text.lower():
                    a = text.split()
                    print(a)
                    x = a.index("do")
                    try:
                        y = a.index("+")
                    except ValueError:
                        try:
                            y = a.index("-")
                        except ValueError:
                            try:
                                y = a.index("*")
                            except ValueError:
                                try:
                                    y = a.index("/")
                                except ValueError:
                                    self.speak("Sorry, you entered wrong mathematical input")
                    number_one = a[x+1:y]
                    print(number_one)
                    number_two = a[y+1:]
                    print(number_two)
                    number_one = "".join(number_one)
                    print(number_one)
                    number_two = "".join(number_two)
                    print(number_two)
                    try:
                        number_one = int(number_one)
                    except ValueError:
                        self.speak("You must say a number to do mathematics")
                    try:
                        number_two = int(number_two)
                    except ValueError:
                        self.speak("You must say a number to do mathematics")
                    if "+" in a:
                        self.speak(f"{number_one} plus {number_two} equals  {number_one + number_two}")
                    elif "-" in a:
                        self.speak(f"{number_one} minus {number_two} equals  {number_one - number_two}")
                    elif "*" in a:
                        self.speak(f"{number_one} times {number_two} equals  {number_one * number_two}")
                    elif "/" in a:
                        try:
                            self.speak(f"{number_one} divided by {number_two} equals  {number_one / number_two}")
                        except ZeroDivisionError:
                            self.speak("You cannot divide with zero!!")
                elif "solve" in text:
                    a = text.split()
                    x = a.index("solve")
                    lesson = a[x+1]
                    if lesson == "algebra":
                        webbrowser.open_new("https://lisari.gr/courses/algevra-a-lykeiou/")
                        self.speak("This is algebra solutions , choose the page and see!!!")
                    elif lesson == "geometry":
                        webbrowser.open_new("https://lisari.gr/courses/geometria-a-lykeiou/")
                        self.speak("This is geometry solutions , choose the page and see!!!")
                    elif lesson == "ancient greek":
                        webbrowser.open_new("https://lisari.gr/courses/archaia-a-lykeiou/")
                        self.speak("This is ancient greek solutions , choose the page and see!!!")
                    elif lesson == "biology":
                        webbrowser.open_new("https://lisari.gr/courses/viologia-a-lykeiou/")
                        self.speak("This is biology solutions , choose the page and see!!!")
                    elif lesson == "english":
                        webbrowser.open_new("https://lisari.gr/courses/anglika-a-lykeiou/")
                        self.speak("This is english solutions , choose the page and see!!!")
                    elif lesson == "french":
                        webbrowser.open_new("https://lisari.gr/courses/gallika-a-lykeiou/")
                        self.speak("This is french solutions , choose the page and see!!!")
                    elif lesson == "physics":
                        webbrowser.open_new("https://lisari.gr/courses/fysiki-a-lykeiou/")
                        self.speak("This is physics solutions , choose the page and see!!!")
                    elif lesson == "chemistry":
                        webbrowser.open_new("https://lisari.gr/courses/chimeia-a-lykeiou/")
                        self.speak("This is chemistry solutions , choose the page and see!!!")
                else:
                    self.speak("I will be upgraded soon so i can understand what you say")

            except:
                self.text_area.insert(tk.END, "Sorry, I could not understand that.\n")

root = tk.Tk()
app = VoiceAssistantGUI(root)
root.mainloop()

