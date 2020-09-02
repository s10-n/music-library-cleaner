# library_cleaner.py - renames album folders in accordance with the album name included in the id3 tags for the files in the album folders
import os,re
from mutagen.id3 import ID3
from mutagen.flac import FLAC
from mutagen.mp4 import MP4
from pathlib import Path
def library_cleaner(library_path):
    # the below regex is used to filter out characters that Windows doesn't like in directory names
    folder_regex = re.compile(r'\*|\\|\||<|>|/|\?|:|"')
    # program starts by cycling through all of the artist subfolders in the main music folder
    for artist_name in os.listdir(library_path):
        # the artist folder path is obtained by combining the main music folder path with the artist name
        artist_folder = library_path + '/' + artist_name
        # the program then iterates through all of the albums in the artist's folder
        for album_name in os.listdir(artist_folder):
            album_folder = artist_folder + '/' + album_name
            # this determines if the first file in the folder is an audio file or not. TODO - could be cleaned up to actually iterate through items in folder
            if os.listdir(album_folder):
                if Path(album_folder + '/' + os.listdir(album_folder)[0]).suffix != '.flac' or '.mp3' or '.m4a':
                    first_track_filename = os.listdir(album_folder)[-1]
                else:
                    first_track_filename = os.listdir(album_folder)[0]
                # if the file is an mp3
                if Path(first_track_filename).suffix == '.mp3':
                    first_track = ID3(album_folder + '/' + first_track_filename)
                    real_album_name =  re.sub(folder_regex,'',first_track['TALB'].text[0])
                    print(f'Renamed {album_name} to {real_album_name}.')
                    os.rename(album_folder,os.path.join(artist_folder,real_album_name))
                # if the file is a flac
                if Path(first_track_filename).suffix == '.flac':
                    first_track = FLAC(album_folder + '/' + first_track_filename)
                    real_album_name =  re.sub(folder_regex,'',first_track['album'][0])
                    print(f'Renamed {album_name} to {real_album_name}.')
                    os.rename(album_folder,os.path.join(artist_folder,real_album_name))
                # if the file is an m4a
                if Path(first_track_filename).suffix == '.m4a':
                    first_track = MP4(album_folder + '/' + first_track_filename)
                    real_album_name =  re.sub(folder_regex,'',str(first_track['\xa9alb'][0]))
                    print(f'Renamed {album_name} to {real_album_name}.')
                    os.rename(album_folder,os.path.join(artist_folder,real_album_name))
