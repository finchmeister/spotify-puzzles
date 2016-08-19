# Zipf's Song Puzzle
# https://labs.spotify.com/puzzles/
# jfinch

import sys


def zips_song(song_input):
    input_list = song_input.split("\n")
    header = input_list.pop(0)
    input_list = filter(None, input_list)
    no_of_songs_to_select = int(header.split(" ")[1])
    songs, index = [], 1.0
    for row in input_list:
        zipfs = float(1/index)
        row_list = row.split(" ")
        plays, name, track_no = int(row_list[0]), row_list[1], int(index)
        songs.append({
            'track_no': track_no,
            'plays': plays,
            'name': name,
            'quality': plays/zipfs,
        })
        index += 1
    songs.sort(key=lambda x: (-x['quality'], x['track_no']))
    ordered_songs = []
    i = 1
    for value in songs:
        ordered_songs.append(value['name'])
        if i == no_of_songs_to_select:
            return "\n".join(ordered_songs)
        i += 1

song_input = sys.stdin.read()
print(zips_song(song_input))