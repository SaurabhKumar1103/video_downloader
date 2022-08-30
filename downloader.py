#import the package
from pytube import YouTube

#wtite this pip install pytube to download pytube
print()
print()
url = 'https://www.youtube.com/watch?v=gYQ6zXzQB9Y'
my_video = YouTube(url)
print("                    ",end="")
print("********Video Title*********")
print()
print()
#get Video Title
print(my_video.title)
print("                    ",end="")
print("*******Tumbnail Image********")
print()
print()
#get Thumbnail Image
print(my_video.thumbnail_url)
print("                    ",end="")
print("*******Download video********")
print()
print()
#get all the stream resolution for the 


#set stream resolution
my_video = my_video.streams.get_highest_resolution()

#or
#my_video = my_video.streams.first()

#Download video
my_video.download()