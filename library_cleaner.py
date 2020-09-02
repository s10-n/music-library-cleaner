# library_cleaner.py - renames album folders in accordance with the album name included in the id3 tags for the files in the album folders
import os,re
from mutagen.id3 import ID3
from mutagen.flac import FLAC
from mutagen.aac import AAC
from mutagen.mp4 import MP4
from pathlib import Path
def library_cleaner():
    library_path = 'c:/Users/User/Projects/library_cleaner/test music'
    for artist_name in os.listdir(library_path):
        artist_folder = library_path + '/' + artist_name
        for album_name in os.listdir(artist_folder):
            album_folder = artist_folder + '/' + album_name
            first_track_filename = os.listdir(album_folder)[0]
            # if the file is an mp3
            first_track = ID3(album_folder + '/' + first_track_filename)
            real_album_name = first_track['TALB'].text[0]
            real_album_name =  re.sub(r'\*|\\|\||<|>|/|\?|:|"','',real_album_name)
            print(os.path.join(artist_folder,real_album_name))
#            os.rename(album_folder,os.path.join(artist_folder,real_album_name))
            # aac
            # alac
            # flac

