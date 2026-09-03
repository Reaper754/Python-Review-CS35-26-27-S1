screen_size = (1920, 1080)

print("Width: ", screen_size[0])
print("Height: ", screen_size[1])

colour = (200, 190, 420)

for i in range(len(colour)):
    if i == 0:
        print("Red: ", colour[i])
    elif i == 1:
        print("Green: ", colour[i])
    else:
        print("Blue: ", colour[i])
