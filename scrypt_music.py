import sys
sys.path.append(r"\DEV\music\lib")
from parsing_music import get_artist_col

dict_music = {}

dict_music = get_artist_col("ц")

print(dict_music)