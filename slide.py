from photo import Photo

class Slide:
  def __init__(self, is_vertical, photos):
    self.id = self.compute_id()
    self.is_vertical = is_vertical
    self.photos = photos
    self.tags = self.compute_tags()
  
  def compute_id(self):
    ids = []
    for photo in self.photos:
      ids.append(photo.id)
    return ' '.join(ids)

  def compute_tags(self):
    tags = set()
    for photo in self.photos:
      for tag in photo.tags:
        tags.add(tag)
    return tags

  def calculate_point(self, other_slide):
    photo = Photo(self.id, self.is_vertical, len(self.tags), self.tags)
    other_photo = Photo(other_slide.id, other_slide.is_vertical, len(other_slide.tags), other_slide.tags)
    return photo.calculate_point(other_photo)
