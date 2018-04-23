import webbrowser
import time

break_counter = 3
while break_counter > 0:
    print("This program started at "+time.ctime())
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=3M_5oYU-IsU")
    break_counter = break_counter - 1