def output(slides,filename):
    lenSlides = len(slides)
    file = filename
    with open(file, 'w') as f:
        f.write('{} '.format(lenSlides))
        f.write('\n')

        for s in slides:
            f.write('{} '.format(s.id))
            f.write('\n')

