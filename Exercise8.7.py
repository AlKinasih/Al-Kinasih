def make_album(artist, title):
    album = {
        "artist": artist,
        "title": title
    }
    return album


album1 = make_album("Taylor Swift", "Midnights")
album2 = make_album("Ariana Grande", "Positions")
album3 = make_album("The Weeknd", "After Hours")

print(album1)
print(album2)
print(album3)