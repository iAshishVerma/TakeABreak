import webbrowser
import time

total_breaks =3
break_count=0
print("Take break on"+time.ctime())
while (break_count <total_breaks):
   time.sleep(10)
   webbrowser.open("https://www.youtube.com/watch?v=NGLxoKOvzu4")
   break_count=break_count+1
