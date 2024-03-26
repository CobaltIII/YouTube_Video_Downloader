import os
from pytube import YouTube
from pytube import Playlist

def time_convertor(a):
    if a <= 59:
        return str(a) + " seconds"
    elif a <= 3599:
        return str(a // 60) + " minutes " + str (a - (( a // 60 )* 60)) + " seconds "
    else:
        return str(a // 3600) + " hours " + str ((a - (( a // 3600 )* 3600)) // 60) + " minutes " + str ((a - (( a // 3600 )* 3600)) - (( (a - (( a // 3600 )* 3600)) // 60 )* 60)) + " seconds "
    
Intro = "Welcome to the Youtube video downloader, A project by Dhruv Jaiswal."
print(Intro)

dump_path = input("Enter the path address to where you want your youtube videos downloaded : ")

Menu = f"""
============================================================
Current directory = {dump_path}
Press 1 to download a video
Press 2 to download a playlist
Press 3 to change directory
Press 4 to exit
=============================================================
"""
print(Menu)
choice = None
while choice != "4":
    if choice != None:
        print(Menu)
    choice = input( "Enter your choice here : ")
    if choice == "1":
        link = input("Input the link of the youtube video you want downloaded : ")
        youtubeobject = YouTube(link)
        
        print("Title:" , youtubeobject.title)
        print("Length of video:" , time_convertor(youtubeobject.length))
        print("Published by:" , youtubeobject.author )
        print("Views:" , youtubeobject.views)
        print("Publish date:" , youtubeobject.publish_date )
        
        print("downloading...")
        
        downloadfile = youtubeobject.streams.get_highest_resolution()
        downloadfile.download(dump_path)
        
        print()
        print("downloaded successfully.")
        
    if choice == "2":
        
        playlistlink = input("Input the link of the youtube playlist you want downloaded : ")
        playlistobject = Playlist(playlistlink)

        cleanedfoldernamelist = [i for i in playlistobject.title.strip() if i not in '/\:*?"<>|']
        cleanedfoldername = ""
        for i in cleanedfoldernamelist:
            cleanedfoldername = cleanedfoldername + i
        path = os.path.join(dump_path , cleanedfoldername.replace(" " , "_"))
        try:
            os.mkdir(path)
            dump_path = path
        except FileExistsError:
            dump_path = path

        listofvideos = playlistobject.videos
        print("Title: " , playlistobject.title)
        print()
        print("Videos in the playlist:")
        listofvideonames = [i.title for i in listofvideos]
        print(*listofvideonames , sep = "\n")
        print()
        print("================download_starting================")
        print()
        for i in listofvideos:        
            print(f"downloading '{i.title}'...")
            print("...")
        
            downloadfile = i.streams.get_highest_resolution()
            downloadfile.download(dump_path)

            print(f"downloaded '{i.title}' successfully.")
            print("\n")
    
        print(f"All videos of the playlist '{playlistobject.title}' are downloaded successfully.")
        
    elif choice == "3":
        dump_path = input("Enter the path address to where you want your youtube videos downloaded : ")
      
