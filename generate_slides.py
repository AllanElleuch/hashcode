from slide import Slide

def generate_slides_from_photos(photos):
  vertical_pool = []
  slides = []

  for photo in photos:
    if photo.is_vertical:
      vertical_pool.append(photo)
    else:
      slide = Slide(False, [photo])
      slides.append(slide)
  
  print('Vertical count:', len(vertical_pool))

  while len(vertical_pool) > 1:
    photo = vertical_pool[0]
    scores = []
    for other_photo in vertical_pool[1:10]:
      score = photo.calculate_point(other_photo)
      scores.append(score)
    best_score_index = scores.index(max(scores))
    slide = Slide(True, [photo, vertical_pool[best_score_index]])
    slides.append(slide)
    del vertical_pool[best_score_index]
    del vertical_pool[0]
  
  return slides
