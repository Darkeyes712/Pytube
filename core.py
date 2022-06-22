from pytube import YouTube
from os import *
import os
from moviepy.editor import AudioFileClip
import shutil

class Downloader_YT(YouTube):

    def __init__(self, link=None) -> None:
        self.link = link
        self.you_tube = YouTube(link)

    def download_highest_resolution(self, path=None):
        """
        Function downloads the video in MP4 format, using the highest resolution. 
        If no path is specifed at the download() function, it will download the file to the script folder.
        """
        self.you_tube.streams.get_highest_resolution().download(path)

    def download_lowest_resolution(self, path=None):
        """
        Function downloads the video in MP4 format, using the lowest resolution. 
        If no path is specifed at the download() function, it will download the file to the script folder.
        """
        self.you_tube.streams.get_lowest_resolution().download(path)

    def download_audio_only(self, path=None):
        """
        Function downloads the video in MP3 format. 
        If no path is specifed at the download() function, it will download the file to the script folder.
        """
        self.you_tube.streams.get_audio_only().download(path)

    def get_video_information(self):
        """
        Get information on the current video. 
        """
        return f'Title: {self.you_tube.title}\n{self.you_tube.length / 60} minutes \n{self.you_tube.views} views\nThe author is: {self.you_tube.author}\n{self.you_tube.description}'


    # Approach using specific folders for file downloads
    @staticmethod
    def rename_download(new_file_name, folder):
        """
        Rename the downloaded resourse to a default name.
        Move the renamed files to the done folder.
        """

        filenames = next(walk(os.path.join(os.getcwd(), f"{folder}")), (None, None, []))[2]  # [] if no file
        file = ''.join(filenames)
        os.rename(os.path.join(os.getcwd(), f"{folder}\\{file}"), os.path.join(os.getcwd(), f"{folder}\\{new_file_name}"))

        file_to_move = os.path.join(os.getcwd(), f"{folder}\\{new_file_name}")
        dest = os.path.join(os.getcwd(), f"{folder}\\done\\{new_file_name}")
        shutil.move(file_to_move, dest)

    @staticmethod
    def convert_mp4_to_mp3(mp4=None, mp3=None):
        """
        Convert the mp4 file to an mp3 format. 
        Delete the mp4 file.
        """
        cur_dir = os.getcwd()
        directory = os.path.join(os.getcwd(), "Audio\\done")

        mp4_without_frames = AudioFileClip(mp4)   
        mp4_without_frames.write_audiofile(mp3)
        mp4_without_frames.close()

        os.chdir(directory)
        all_files = os.listdir()
        for file in all_files:
            if file.endswith('mp4'):
                os.remove(file)
        os.chdir(cur_dir)

    

# d = Downloader_YT('https://www.youtube.com/watch?v=IYNO5-8kC5U&list=RDIYNO5-8kC5U&start_radio=1')
# print(d.get_video_information())