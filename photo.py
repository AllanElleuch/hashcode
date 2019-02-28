class Photo:
  def __init__(self, is_vertical, nb_tags, tags):
    self.is_vertical = is_vertical
    self.tags = tags
    self.nb_tags = len(tags)

  def __repr__(self):
        return "is vertical : " + str(self.is_vertical) +" nbtags : " + self.nb_tags + " tags : ".join(self.tags)  


  def calculate_point(self, other_photo):
    return min(
      self.common_tags(other_photo),
      self.tags_not_in_other(other_photo),
      self.other_tags_not_in_ours(other_photo)
    ) 
  
  def common_tags(self, other_photo):
    tags = set()
    for tag in other_photo.tags:
      if tag in self.tags:
        tags.add(tag)
    return len(tags)
  
  def tags_not_in_other(self, other_photo):
    tags = set()
    for tag in self.tags:
      if tag not in other_photo.tags:
        tags.add(tag)
    return len(tags)
  
  def other_tags_not_in_ours(self, other_photo):
    tags = set()
    for tag in other_photo.tags:
      if tag not in self.tags:
        tags.add(tag)
    return len(tags)
