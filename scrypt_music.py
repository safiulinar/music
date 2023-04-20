import sys
sys.path.append(r"\DEV\music\lib")
from parsing_music import get_artist_col

dict_music = {}
dict_music = get_artist_col("я")

print(dict_music)

#for l in dict_music.keys():
#    print(l)
#    for n in dict_music[l].keys():
#        for m in range(len(dict_music[l][n])):
#            print(dict_music[l][n][m])