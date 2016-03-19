#JOKER OUTPUT FILE [1]
from random import randint

jokes = [
"I asked my North Korean friend how it was there, he said he couldn't complain.",
"There's no 'I' in Denial.",
"What's the best thing about Switzerland? I don't know, but their flag is a huge plus."
]

file = open("joke.txt", "w")
file.write(jokes[randint(0, len(jokes)-1)])
file.close()
