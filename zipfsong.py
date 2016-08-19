# Zipf's Song Puzzle
# https://labs.spotify.com/puzzles/
# jfinch

import sys


def zips_song(song_input):
    input_list = song_input.split("\n")
    header = input_list.pop(0)
    input_list = filter(None, input_list)
    header_list = header.split(" ")
    no_of_songs, no_of_songs_to_select = int(header_list[0]), int(header_list[1])
    songs, index = [], 1
    for row in input_list:
        row_list = row.split(" ")
        songs.append({
            'track_no': index,
            'plays': row_list[0],
            'name': row_list[1],
            'quality': int(row_list[0])*index,
        })
        if index == no_of_songs:
            break
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