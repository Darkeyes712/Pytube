from tkinter import *
from tkinter import messagebox
from core import *
from config import *

# this shit creates the window
window = Tk()
# setting the frame
window.geometry("800x600")
# disabling the resize option of the window for better UX
window.resizable(0, 0)
# title of the program
window.title("Kolzo's YouTube Downloader")


# Images
photo = PhotoImage(file="img/bg.png")
photoimage = photo.subsample(1, 1)
###
options = PhotoImage(file="img/g.png")
photoimage_options = options.subsample(1, 1)

# Background
frame_logo = Label(window, image=photoimage).place(anchor=CENTER, relx=0.5, rely=0.5,)

video_link = StringVar()
destination_path = StringVar()

def clear_text():
    entry_field.delete(0, END)

entry_field = Entry(window, width=70, borderwidth=10, textvariable=video_link)
entry_field.place(relx=0.5, rely=0.7, anchor=CENTER)

def download_high_resolution():
    
    url = str(video_link.get())
    c = Configs()
    d = Downloader_YT(url)
    d.download_highest_resolution(os.path.join(os.getcwd(), "Video_High"))
    d.rename_download(new_file_name=f"converted_high_{c.random_id_generator()}.mp4", folder="Video_High")

def download_low_resolution():

    url = str(video_link.get())
    c = Configs()
    d = Downloader_YT(url)
    d.download_lowest_resolution(os.path.join(os.getcwd(), "Video_Low"))
    d.rename_download(new_file_name=f"converted_low_{c.random_id_generator()}.mp4", folder="Video_Low")

def download_audio_only():

    url = str(video_link.get())
    c = Configs()
    d = Downloader_YT(url)
    new_file_name = f"converted_{c.random_id_generator()}"
    d.download_audio_only(os.path.join(os.getcwd(), "Audio"))
    d.rename_download(new_file_name=f"{new_file_name}.mp4", folder="Audio")
    d.convert_mp4_to_mp3(mp4=os.path.join(os.getcwd(), f"Audio\\done\\{new_file_name}.mp4"), mp3=os.path.join(os.getcwd(), f"Audio\\done\\{new_file_name}.mp3"))
    

# Feature buttons
button_clear= Button(window,
                    background="gray",
                    text="Clear Field",
                    width=10, 
                    height=1, 
                    padx=3, 
                    pady=1, 
                    font=("Arial", 12, "bold"),
                    anchor=CENTER,
                    command=clear_text
                    ).place(
                        relx=0.5, 
                        rely=0.8, 
                        anchor=CENTER)
button_hq= Button(window,
                    background="gray",
                    text="High Quality",
                    width=10, 
                    height=3, 
                    padx=3, 
                    pady=1, 
                    font=("Arial", 12, "bold"),
                    anchor=CENTER,
                    command=download_high_resolution
                    ).place(
                        relx=0.3, 
                        rely=0.9, 
                        anchor=CENTER)
button_lq = Button(window,
                    background="gray",
                    text="Low Quality",
                    width=10, 
                    height=3, 
                    padx=3, 
                    pady=1,
                    font=("Arial", 12, "bold"), 
                    anchor=CENTER, 
                    command=download_low_resolution
                    ).place(
                        relx=0.5, 
                        rely=0.9, 
                        anchor=CENTER)
button_mp3 = Button(window,
                    background="gray",
                    text="MP3",
                    width=10, 
                    height=3, 
                    padx=3, 
                    pady=1,
                    font=("Arial", 12, "bold"), 
                    anchor=CENTER, 
                    command=download_audio_only
                    ).place(
                        relx=0.7, 
                        rely=0.9, 
                        anchor=CENTER)

# Options button
button_options = Button(window,
                    background="gray",
                    image=photoimage_options,
                    width=70, 
                    height=70, 
                    padx=3, 
                    pady=1, 
                    anchor=CENTER, 
                    command=lambda: messagebox.showerror("Not Yet, Moron!", "Feature is under construction!")
                    ).place(
                        relx=0.9, 
                        rely=0.1, 
                        anchor=CENTER)


# This is essential to keep the window open:
window.mainloop()
