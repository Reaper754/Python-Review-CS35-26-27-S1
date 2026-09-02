games = ["Minecraft", "Portal", "Tetris"]

games.append("Celeste")
games.append("astroneer")
games[3]="Mario"

for game in games:
    print(game)
print(len(games))
print("==================")

numbers = [3, 10, 5, 6, 8]
total = [1]
for i in range(len(numbers)):
    if i == 0:
        total[0]=numbers[i]
        print(total[0])
    else:
        total[0] = total[0] + numbers[i]
        print(total[0])