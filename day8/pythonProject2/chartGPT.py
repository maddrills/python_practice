from enumerateShit import albums

SONGS_LIST_INDEX = 3

while True:
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{0}: {1}".format(index + 1, title, artist, year, songs))

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice -1][SONGS_LIST_INDEX]
    else:
        break

    print(albums[choice -1])
    print(songs_list)
    print()