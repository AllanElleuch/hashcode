from slide import Slide

def order_slides(slides):
  reordered_slides = []

  while len(slides) > 1:
    slide = slides[0]
    scores = []
    for other_slide in slides[1:10]:
      score = slide.calculate_point(other_slide)
      scores.append(score)
    best_score_index = scores.index(max(scores))  +1
    reordered_slides.append(slide)
    reordered_slides.append(slides[best_score_index])
    del slides[best_score_index]
    del slides[0]
  
  return reordered_slides
