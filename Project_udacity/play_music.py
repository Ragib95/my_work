#play youtube music
import webbrowser
import time

count = 1
while count <= 10:
	time.sleep(3)
	webbrowser.open_new('https://www.youtube.com/watch?v=kclXuc_J50Y')
	count = count + 1