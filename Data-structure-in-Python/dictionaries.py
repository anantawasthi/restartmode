counts = dict()
line = "So now we're going to combine all this together. We're going to read some data, we're going to read a file, we're going to make some dictionaries, we're going to make some lists. And we're going to use all these things to build a real program. So what the real program is going to solve... and so let's see if you can solve this, right? Read this text really quick, like in a hundredth of a second or so and figure out what the most common word is and how many of these things there are. It's kind of like the problem we showed you before, except I was showing you names. So figure it out. What is the most common word and how many are there? Or maybe, let's just skip to the next slide, because humans are so bad at this. I mean, humans are looking at this and saying like, um, no, I refuse to do this, as compared to the other ones we actually tried. Now we're not even going to try. It's like dude, how about we just write some Python code to solve this problem? I know how this turns out. We've seen this story before. Okay. So here's the basic pattern."
print(line)

words = line.split()

print("words ", words )

print('counting ....')

for word in words:
    counts[word] = counts.get(word, 0) + 1
print('counts', counts)
 
stuff = dict()
stuff['candy']

stuff.get('candy', -1)