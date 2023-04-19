import sys
sys.path.append(r"\DEV\music\lib")
from parsing_music import get_artist_col

dict_music = {}
dict_music = get_artist_col("ц")

for l in dict_music.keys():
    for n in dict_music[l].keys():
        for m in range(len(dict_music[l][n])):
            print(dict_music[l][n][m])