from inspect import getcallargs
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from core import Downloader_YT, Downloader_YT_Playlist
from config import *
from thread_frm import KThread
import pygame
import os
import sys

# this shit creates the window
window = Tk()
# setting the frame
window.geometry("800x600")
# disabling the resize option of the window for better UX
window.resizable(0, 0)
# title of the program
window.title("Kolzo's YouTube Downloader")
# Background image
photo = PhotoImage(file="img/bg.png")
photoimage = photo.subsample(1, 1)
# Options menu image
options = PhotoImage(file="img/g.png")
photoimage_options = options.subsample(1, 1)
# Volume image
volume = PhotoImage(file="img/volume.png")
photoimage_volume = volume.subsample(1, 1)
# Mute image
mute = PhotoImage(file="img/mute.png")
photoimage_mute = mute.subsample(1, 1)
# Assigning background
frame_logo = Label(window, image=photoimage).place(anchor=CENTER, relx=0.5, rely=0.5,)
# Assining string variables
video_link = StringVar()
download_path = StringVar()
#destination_path = StringVar() # this may be needed later on
# Creating the Entry field
entry_field = Entry(window, width=70, borderwidth=10, textvariable=video_link)
entry_field.place(relx=0.5, rely=0.7, anchor=CENTER)
#Adding software icon
window.iconbitmap('img/burglar.ico')

def clear_text():
    """
    Function clears the entry filed of all text once the Clear Filed button is pressed.
    """
    entry_field.delete(0, END)

def play_music():
    """
    Function loads audio file as background music.
    Function is triggered on button click. 
    """
    def get_script_path():
        return os.path.dirname(os.path.realpath(sys.argv[0]))

    project_dir = get_script_path()
    os.chdir(project_dir)
    pygame.mixer.music.load(os.path.join(os.getcwd(),'audio/nkg.mp3'))
    pygame.mixer.music.play()

def stop_music():
    """
    Function stops the background music on click. 
    """
    pygame.mixer.music.stop()

def get_video_info():
    """
    Function ivokes the Downloader class and adds the get information functionality to the corresponding button.
    """
    url = str(video_link.get())
    d = Downloader_YT(url)

    return d.get_video_information()

def get_playlist_info():
    """
    Function ivokes the Downloader_Playlist class and adds the get information functionality to the corresponding button.
    """
    url = str(video_link.get())
    d = Downloader_YT_Playlist(url)

    return d.get_playlist_info()

def download_high_resolution():
    """
    Function ivokes the Downloader class and adds the high resolution functionality to the corresponding button.
    Function asks for user to choose a download path and the file gets downloaded there.
    """
    url = str(video_link.get())
    d = Downloader_YT(url)
    download_directory = filedialog.askdirectory(initialdir="Input File Path Here")
    download_path.set(download_directory)

    thread = KThread(target = d.download_highest_resolution, daemon=True, kwargs={'path': download_path.get()})
    thread.start()

    return messagebox.showinfo("In Progress!", f"Video file will be downloaded in {download_path.get()}")

def download_low_resolution():
    """
    Function ivokes the Downloader class and adds the low resolution functionality to the corresponding button.
    Function asks for user to choose a download path and the file gets downloaded there.
    """
    url = str(video_link.get())
    d = Downloader_YT(url)
    download_directory = filedialog.askdirectory(initialdir="Input File Path Here")
    download_path.set(download_directory)

    thread = KThread(target = d.download_lowest_resolution, daemon=True, kwargs={'path': download_path.get()})
    thread.start()

    return messagebox.showinfo("In Progress!", f"Video file will be downloaded in {download_path.get()}")

def download_audio_only():
    """
    Function ivokes the Downloader class and adds the audio only functionality to the corresponding button.
    Function asks for user to choose a download path and the file gets downloaded there.
    """
    url = str(video_link.get())
    d = Downloader_YT(url)
    download_directory = filedialog.askdirectory(initialdir="Input File Path Here")
    download_path.set(download_directory)

    thread = KThread(target = d.download_audio_only, daemon=True, kwargs={'path': download_path.get()})
    thread.start()
    
    messagebox.showinfo("In Progress!", f"Audio file will be downloaded in {download_path.get()}")

def download_playlist_high_resolution():
    """
    Function ivokes the Downloader class and adds the high resolution functionality to the corresponding button.
    Function asks for user to choose a download path and the file gets downloaded there.
    """
    url = str(video_link.get())
    d = Downloader_YT_Playlist(url)
    download_directory = filedialog.askdirectory(initialdir="Input File Path Here")
    download_path.set(download_directory)

    thread = KThread(target = d.download_all_content_from_playlist_in_high_quality, daemon=True, kwargs={'path': download_path.get()})
    thread.start()

    return messagebox.showinfo("In Progress!", f"Video file will be downloaded in {download_path.get()}")

def download_playlist_low_resolution():
    """
    Function ivokes the Downloader class and adds the low resolution functionality to the corresponding button.
    Function asks for user to choose a download path and the file gets downloaded there.
    """
    url = str(video_link.get())
    d = Downloader_YT_Playlist(url)
    download_directory = filedialog.askdirectory(initialdir="Input File Path Here")
    download_path.set(download_directory)

    thread = KThread(target = d.download_all_content_from_playlist_in_low_quality, daemon=True, kwargs={'path': download_path.get()})
    thread.start()

    return messagebox.showinfo("In Progress!", f"Video file will be downloaded in {download_path.get()}")

def download_playlist_audio_only():
    """
    Function ivokes the Downloader class and adds the audio only functionality to the corresponding button.
    Function asks for user to choose a download path and the file gets downloaded there.
    """
    url = str(video_link.get())
    d = Downloader_YT_Playlist(url)
    download_directory = filedialog.askdirectory(initialdir="Input File Path Here")
    download_path.set(download_directory)

    thread = KThread(target = d.download_all_content_from_playlist_in_mp3, daemon=True, kwargs={'path': download_path.get()})
    thread.start()
    
    messagebox.showinfo("In Progress!", f"Audio file will be downloaded in {download_path.get()}")

# Feature buttons
button_volume= Button(window,
                    background="green",
                    image=photoimage_volume,
                    padx=3, 
                    pady=1, 
                    font=("Arial", 12, "bold"),
                    anchor=CENTER,
                    command=play_music
                    ).place(
                        relx=0.1, 
                        rely=0.1, 
                        anchor=CENTER)
button_mute= Button(window,
                    background="red",
                    image=photoimage_mute,
                    padx=3, 
                    pady=1, 
                    font=("Arial", 12, "bold"),
                    anchor=CENTER,
                    command=stop_music
                    ).place(
                        relx=0.2, 
                        rely=0.1, 
                        anchor=CENTER)
button_info= Button(window,
                    background="silver",
                    text="Get Video Info",
                    width=15, 
                    height=1, 
                    padx=3, 
                    pady=1, 
                    font=("Arial", 12, "bold"),
                    anchor=CENTER,
                    command=lambda: messagebox.showinfo("Video Information", f"{get_video_info()}")
                    ).place(
                        relx=0.3, 
                        rely=0.8, 
                        anchor=CENTER)
button_playlist_info= Button(window,
                    background="silver",
                    text="Get Playlist Info",
                    width=15, 
                    height=1, 
                    padx=3, 
                    pady=1, 
                    font=("Arial", 12, "bold"),
                    anchor=CENTER,
                    command=lambda: messagebox.showinfo("Playlist Information", f"{get_playlist_info()}")
                    ).place(
                        relx=0.7, 
                        rely=0.8, 
                        anchor=CENTER)
button_clear= Button(window,
                    background="silver",
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
button_playlist_hq = Button(window,
                    background="gray",
                    text="Playlist High Quality",
                    width=15, 
                    height=3, 
                    padx=3, 
                    pady=1,
                    font=("Arial", 12, "bold"), 
                    anchor=CENTER, 
                    command=download_playlist_high_resolution
                    ).place(
                        relx=0.2, 
                        rely=0.3, 
                        anchor=CENTER)
button_playlist_lq = Button(window,
                    background="gray",
                    text="Playlist Low Quality",
                    width=15, 
                    height=3, 
                    padx=3, 
                    pady=1,
                    font=("Arial", 12, "bold"), 
                    anchor=CENTER, 
                    command=download_playlist_low_resolution
                    ).place(
                        relx=0.5, 
                        rely=0.3, 
                        anchor=CENTER)
button_playlist_mp3 = Button(window,
                    background="gray",
                    text="Playlist MP3",
                    width=15, 
                    height=3, 
                    padx=3, 
                    pady=1,
                    font=("Arial", 12, "bold"), 
                    anchor=CENTER, 
                    command=download_playlist_audio_only
                    ).place(
                        relx=0.8, 
                        rely=0.3, 
                        anchor=CENTER)
button_options = Button(window,
                    background="gray",
                    image=photoimage_options,
                    width=70, 
                    height=70, 
                    padx=3, 
                    pady=1, 
                    anchor=CENTER, 
                    command=lambda: messagebox.showinfo("Information Below!", 
                        "The Playlist buttons work only with a link for the playlist itself.\n\n"\
                        "The Regular buttons work with a link to a single video only.\n\n"\
                        "The Clear field button removes any text from the Entry field.\n\n"\
                        "The Get Video Info button provides all information for a single video.\n\n"\
                        "The Get Playlist Info button provides all information for all the videos in a playlist.\n\n")
                    ).place(
                        relx=0.9, 
                        rely=0.1, 
                        anchor=CENTER)

# This is essential to keep the window open:
window.mainloop()
