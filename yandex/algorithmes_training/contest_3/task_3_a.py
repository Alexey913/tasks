# n = int(input())
# common_songs = []
# for _ in range(n):
#     count = int(input())
#     common_songs += input().split()
# if n == 1:
#     print(len(common_songs))
#     print(" ".join(common_songs))
# else:
#     final_playlist = set([i for i in common_songs if common_songs.count(i) > 1])
#     print(len(final_playlist))
#     print(" ".join(final_playlist))


n = int(input())
common_songs = {}
for _ in range(n):
    count = int(input())
    for i in input().split():
        if i in common_songs:
            common_songs[i] += 1
        else:
            common_songs[i] = 1
if n == 1:
    print(len(common_songs))
    print(" ".join(sorted(common_songs)))
else:
    final_playlist = {k for k, v in common_songs.items() if v == n}
    print(len(final_playlist))
    print(" ".join(sorted(final_playlist)))