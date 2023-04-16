from pytube import YouTube
from tkinter import filedialog
import webbrowser

print("Created by : Mahmoud Mohamed Mahmoud @ 2023 \n")
url_input = input("Please Enter Your Youtube URL : ")
print("\n")
beef_list = ["Open", "Download"]
beef = 0
for i in beef_list:
    beef = beef+1
    print(f"{beef} : {i}")
print("\n")
choosing = int(input("Please Choose Process : "))

if choosing == 1:
    webbrowser.open(url_input)
else:
    all_streams = YouTube(url_input).streams.all()
    v = -1
    for i in all_streams:
        v = v+1
        print(str(v)+" : "+str(i))
    stm_input = int(input("Please Choose The Suitable Stream : "))
    print("Please Choose Directory To Save : ) ")
    folder_name = filedialog.askdirectory()
    choice = all_streams[stm_input].download(folder_name)

    print("Download Complete ............. \n")