#DIB DAB FILLER [3]
from random import randint

randomTotal = randint(51, 270)

file = open("dibdab.txt", "w")
for i in range(randomTotal):
    if randint(1,4) == 1:
        file.write("dib\n")
    else: 
        file.write("dab\n")

file.close()
