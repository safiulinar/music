import sys
sys.path.append(r"\DEV\music\lib")
from parsing_music import get_artist_col
from parsing_music import load_in_db

dict_music = {}
dict_music = get_artist_col("а")

print(dict_music)

#l = load_in_db(dict_music)

