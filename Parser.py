def parser(file):
    photos = []
    with open(file, 'r') as f:
        for i, line in enumerate(f):
            if i == 0: nbRow = line.split(' ')
            else:
                line = line.rstrip('\r\n')
                orientation,numberTag, *tags =  line.split(' ') #orientation = V/H
                print(tags)
                photos.append("a") #replace with constructor of a photo
    return photos #rides, int(rows), int(cols), int(n_vehicles), int(bonus), int(t)

#to test
#parser("./a_example.txt")

