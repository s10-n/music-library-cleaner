# library_cleaner.py - renames album folders in accordance with the album name included in the id3 tags for the files in the album folders
import os,re
from mutagen.id3 import ID3
from mutagen.flac import FLAC
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
            if Path(first_track_filename).suffix == '.mp3':
                first_track = ID3(album_folder + '/' + first_track_filename)
                real_album_name = first_track['TALB'].text[0]
                real_album_name =  re.sub(r'\*|\\|\||<|>|/|\?|:|"','',real_album_name)
                print(os.path.join(artist_folder,real_album_name))
                os.rename(album_folder,os.path.join(artist_folder,real_album_name))
            # if the file is a flac
            if Path(first_track_filename).suffix == '.flac':
                first_track = FLAC(album_folder + '/' + first_track_filename)
#                real_album_name = first_track['TALB'].text[0]
                real_album_name =  re.sub(r'\*|\\|\||<|>|/|\?|:|"','',first_track['album'][0])
                print(os.path.join(artist_folder,real_album_name))
                os.rename(album_folder,os.path.join(artist_folder,real_album_name))
            if Path(first_track_filename).suffix == '.m4a':
                # if the file is an m4a
 #               print(album_folder + '/' + first_track_filename)
  #              print(MP4(album_folder + '/' + first_track_filename)['\xa9alb'])
                first_track = MP4(album_folder + '/' + first_track_filename)
#                real_album_name = str(first_track['\xa9alb']).strip("[']")
                real_album_name =  re.sub(r'\*|\\|\||<|>|/|\?|:|"','',str(first_track['\xa9alb'][0]))
                print(os.path.join(artist_folder,real_album_name))
                os.rename(album_folder,os.path.join(artist_folder,real_album_name))






library_cleaner()
