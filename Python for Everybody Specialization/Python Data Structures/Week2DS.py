
fh = open(r"Python for Everybody Specialization\Python Data Structures\W3.txt", 'r')
fh

counter = 0
lst = list()
for line in fh:
    splt = line.rstrip().split()
    for word in splt:
        if word not in lst:
            lst.append(word)

lst
lst.sort()

