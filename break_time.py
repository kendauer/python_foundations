import time
import webbrowser

total_breaks = 3
break_count = 0

while (break_count < total_breaks):
    time.sleep(1)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    i = i + 1
print i
