from pytube import YouTube, Playlist
from os import *
import os
from moviepy.editor import AudioFileClip
import shutil

class Downloader_YT(YouTube):

    def __init__(self, video_link=None, playlist_link=None) -> None:

        self.you_tube = YouTube(video_link)
        self.playlist = Playlist(playlist_link)

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
        file_name = self.get_content_name()
        self.convert_mp4_to_mp3(file_name, path)

    def get_content_name(self):
        """
        Function gets the file name and returns a string.
        """
        return str(self.you_tube.streams.first().default_filename)

    def get_video_information(self):
        """
        Get information on the current video. 
        """
        return f'Title: {self.you_tube.title}\n{self.you_tube.length / 60} minutes \n{self.you_tube.views} views\nThe author is: {self.you_tube.author}\n{self.you_tube.description}'

    # Approach using specific folders for file downloads
    @staticmethod
    def rename_download_for_backend_version(new_file_name, folder):
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
    def convert_mp4_to_mp3_for_backend_version(mp4=None, mp3=None):
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

    @staticmethod
    def convert_mp4_to_mp3(file, path_):
        """
        Function takes 2 arguments:
            file - the name of the file.
            path_ = the file path where the file is downloaded.
        Function converts the mp4 file to mp3 and deletes all mp4 files from the folder. 
        """
        current_path = os.path.abspath(path_)
        os.chdir(current_path)

        # Testing
        cwd = os.getcwd()
        print(str(cwd))

        base, ext = os.path.splitext(file)
        old_file = base + '.mp4'
        # Testing
        print(old_file)

        base, ext = os.path.splitext(file)
        new_file = base + '.mp3'
        # Testing
        print(new_file)
        
        mp4_without_frames = AudioFileClip(os.path.join(current_path, old_file))   
        mp4_without_frames.write_audiofile(os.path.join(current_path, new_file))
        mp4_without_frames.close()
        os.remove(old_file)

class Downloader_YT_Playlist(Playlist):

    def __init__(self, playlist_link=None) -> None:

        self.playlist = Playlist(playlist_link)

    def download_all_content_from_playlist_in_high_quality(self, path=None):
        """
        Function downloads all videos from a playlist in the highest possible resolution. 
        If no path is specifed at the download() function, it will download the file to the script folder.
        """
        for i in self.playlist.videos:
            i.streams.get_highest_resolution().download(path)
        
    def download_all_content_from_playlist_in_low_quality(self, path=None):
        """
        Function downloads all videos from a playlist in the lowest possible resolution. 
        If no path is specifed at the download() function, it will download the file to the script folder.
        """
        for i in self.playlist.videos:
            i.streams.get_lowest_resolution().download(path)

    def download_all_content_from_playlist_in_mp3(self, path=None):
        """
        Function downloads all videos from a playlist in audio format then convert them to mp3. 
        If no path is specifed at the download() function, it will download the file to the script folder.
        """
        for i in self.playlist.videos:
            i.streams.get_audio_only().download(path)
            file_name = i.streams.first().default_filename
            Downloader_YT.convert_mp4_to_mp3(file_name, path)
        
    def get_playlist_info(self):
        """
        This function uses the generator approach to returning multiple items from a function.
            1. Get information for every video of the playlist inside the nested function and create a generated object, using the yiled keyword.
            2. Use list comprehension on the nested function to aquire all of the results and put them in a string.

        """
        def create_generator_object():

            for i in self.playlist.videos:
                yield f'Title: {i.title}\n{i.length / 60} minutes \n{i.views} views\nThe author is: {i.author}\n{i.description}\n\n'

        list_of_items = [''.join(i) for i in create_generator_object()]
        final_item = ' '.join(list_of_items)

        return final_item  
            
