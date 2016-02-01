class Club:
    'Class which creates a new club with name and points'
    def __init__(self, name, points):
        global clubs
        self.name = name
        self.points = points

clubOne = Club("One", 23)
clubTwo = Club("Two", 43)
clubThree = Club("Three", 21)

clubs = [clubOne.points, clubTwo.points, clubThree.points]
clubs.sort()
print(clubs)
