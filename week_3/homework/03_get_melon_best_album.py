genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    genres = {}
    song_indexes = list(range(len(genre_array)))

    for i in song_indexes:
        genres[genre_array[i]] = 0
    for i in song_indexes:
        genres[genre_array[i]] += plays[i]
    sorted_genres = sorted(genres.items(), key=lambda x: x[1], reverse=True)
    print(sorted_genres)
    merged_list = []
    for i in song_indexes:
        merged_list.append((i, genre_array[i], play_array[i]))
    sorted_songs = sorted(merged_list, key=lambda x: x[2], reverse=True)
    print(sorted_songs)
    result = []
    for genre in sorted_genres:
        count = 0
        for song in sorted_songs:
            if song[1] == genre[0]:
                result.append(song[0])
                count += 1
            if count > 1:
                break

    return result

print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!