game = {
    "title": "Tetris",
    "year": 1985,
    "players": 1
}
game["device"] = "gameboy"
game["units sold"] = 520000000

for key, value in game.items():
    print(f"{key}: {value}")

character = {
    "name": "Reaper",
    "health": 120,
    "level": 34,
    "character class": "assault"
}

for key, value in character.items():
    print(f"{key}: {value}")

character["health"] = 100

for key, value in character.items():
    print(f"{key}: {value}")