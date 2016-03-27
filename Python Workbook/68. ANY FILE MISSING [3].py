#ANY FILE MISSING [3]
for i in range(3):
    try:
        with open("{}.txt".format(i+1)) as f:
            print((f.readlines())[0])
    
    except FileNotFoundError:
        print("File {} is missing".format(i+1))
