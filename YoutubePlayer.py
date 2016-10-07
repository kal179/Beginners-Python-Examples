import webbrowser
import random

youtubeMusic = ["https://www.youtube.com/watch?v=6pR5cyH63mA", "https://www.youtube.com/watch?v=4JK_Lg8P7PU", "https://www.youtube.com/watch?v=nbjwmC8K4K4", "https://www.youtube.com/watch?v=qHm9MG9xw1o", "https://www.youtube.com/watch?v=QJO3ROT-A4E"]

user = str(raw_input("Start playing : "))
if user == "No":
    exit()

playingStyle = str(raw_input("Play in order or random song : "))

if user == "Yes" and playingStyle == "random song":
    webbrowser.open(random.choice(["https://www.youtube.com/watch?v=6pR5cyH63mA", "https://www.youtube.com/watch?v=4JK_Lg8P7PU", "https://www.youtube.com/watch?v=nbjwmC8K4K4", "https://www.youtube.com/watch?v=qHm9MG9xw1o", "https://www.youtube.com/watch?v=QJO3ROT-A4E"]))
elif user == "Yes" and playingStyle == "Play in order":
    for x in youtubeMusic:
        webbrowser.open(x)
