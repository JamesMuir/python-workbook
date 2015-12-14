#Comma code
spam = ['apples', 'bananas', 'tofu', 'cats']

def commaCode(theList):
    for i in theList:
        if i == theList[-1]:
            print(i)
        else:
            print(i, end=", ")

commaCode(spam)
