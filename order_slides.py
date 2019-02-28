from slide import Slide

def order_slides(slides):
  reordered_slides = []

  while len(slides) > 1:
    photo = slides[0]
    scores = []
    for other_photo in slides[1:10]:
      score = photo.calculate_point(other_photo)
      scores.append(score)
    best_score_index = scores.index(max(scores))
    slide = Slide(True, [photo, slides[best_score_index]])
    reordered_slides.append(slide)
    del slides[best_score_index]
    del slides[0]
  
  return reordered_slides
