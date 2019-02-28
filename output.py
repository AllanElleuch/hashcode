def output(slides):
    lenSlides = len(slides)
    file = "out.txt"
    with open(file, 'w') as f:
        f.write('{} '.format(lenSlides))
        f.write('\n')

        for s in slides:
            f.write('{} '.format(s.id))
            f.write('\n')

