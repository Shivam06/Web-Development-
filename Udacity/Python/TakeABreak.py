import webbrowser
import time

def take_breaks(break_count):
    for i in range(break_count):
        print time.ctime()
        time.sleep(10)
        webbrowser.open("https://www.youtube.com/watch?v=-qlJiGGvPUI")

take_breaks(3)
