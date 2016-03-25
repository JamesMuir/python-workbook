#READ AND COUNT [4]
with open("numbers.txt") as f:
    fileContent = f.readlines()

numberStrings = fileContent[0].split()

total = 0
for i in numberStrings:
    total += float(i)

print(total)
