#NOTE Make a functionality that lets the user save the file where he chooses
#from tkinter.filedialog import asksaveasfile # used to save a file 




# Use this to test the backend part: 

# d = Downloader_YT('https://www.youtube.com/watch?v=rzDPk8tqwvQ&list=RDrzDPk8tqwvQ&index=2')

# def run_audio():
#     d.download_audio_only(os.path.join(os.getcwd(), "Audio"))
#     d.rename_download(new_file_name="converted.mp4", folder="Audio")
#     d.convert_mp4_to_mp3(mp4=os.path.join(os.getcwd(), "Audio\\converted.mp4"), mp3=os.path.join(os.getcwd(), "Audio\\audio_converted.mp3"))
# def run_video_low():
#     d.download_lowest_resolution(os.path.join(os.getcwd(), "Video_Low"))
#     d.rename_download(new_file_name="converted_low.mp4", folder="Video_Low")
# def run_video_high():
#     d.download_highest_resolution(os.path.join(os.getcwd(), "Video_High"))
#     d.rename_download(new_file_name="converted_high.mp4", folder="Video_High")



#NOTE Below functions are used if you want to use the specific folder structure approach for the Downloader App
#NOTE These functions should be in the main.py file and assigned to the buttons:

# def download_high_resolution():
#     """
#     Function ivokes the Downloader class and adds the high resolution functionality to the corresponding button.
#     """
#     url = str(video_link.get())
#     c = Configs()
#     d = Downloader_YT(url)
#     d.download_highest_resolution(os.path.join(os.getcwd(), "Video_High"))
#     d.rename_download(new_file_name=f"converted_high_{c.random_id_generator()}.mp4", folder="Video_High")

# def download_low_resolution():
#     """
#     Function ivokes the Downloader class and adds the low resolution functionality to the corresponding button.
#     """
#     url = str(video_link.get())
#     c = Configs()
#     d = Downloader_YT(url)
#     d.download_lowest_resolution(os.path.join(os.getcwd(), "Video_Low"))
#     d.rename_download(new_file_name=f"converted_low_{c.random_id_generator()}.mp4", folder="Video_Low")

# def download_audio_only():
#     """
#     Function ivokes the Downloader class and adds the audio only functionality to the corresponding button.
#     """
#     url = str(video_link.get())
#     c = Configs()
#     d = Downloader_YT(url)
#     new_file_name = f"converted_{c.random_id_generator()}"
#     d.download_audio_only(os.path.join(os.getcwd(), "Audio"))
#     d.rename_download(new_file_name=f"{new_file_name}.mp4", folder="Audio")
#     d.convert_mp4_to_mp3(mp4=os.path.join(os.getcwd(), f"Audio\\done\\{new_file_name}.mp4"), mp3=os.path.join(os.getcwd(), f"Audio\\done\\{new_file_name}.mp3"))