import subprocess
import shutil
from win32com.client import Dispatch
import os, winshell

def pack():
    """
    Function creates all the nessesary resources for the program to run using an executable file.
    """
    subprocess.run('pyinstaller --noconsole --icon=bin/img/burglar.ico bin/youtube_downloader.py')
    source_dir = os.path.join(os.getcwd(), 'bin', 'img')
    destination_dir = os.path.join(os.getcwd(), 'dist', 'youtube_downloader', 'img')
    shutil.copytree(source_dir, destination_dir)

    source_dir_2 = os.path.join(os.getcwd(), 'bin', 'audio')
    destination_dir_2 = os.path.join(os.getcwd(), 'dist', 'youtube_downloader', 'audio')
    shutil.copytree(source_dir_2, destination_dir_2)

def shortcut():
    """
    Create a shortcut of an .exe file and paste it at the Desktop directory.
    """
    desktop = winshell.desktop()
    path = os.path.join(desktop, "youtube_downloader.lnk")
    target = os.path.join(os.getcwd(), 'dist', 'youtube_downloader', 'youtube_downloader.exe')
    wDir = os.path.join(os.getcwd(), 'dist', 'youtube_downloader')
    icon = os.path.join(os.getcwd(), 'dist', 'youtube_downloader', 'youtube_downloader.exe')

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    shortcut.IconLocation = icon
    shortcut.save()



pack()
shortcut()