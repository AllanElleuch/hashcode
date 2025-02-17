class Photo:
  def __init__(self, identifier, is_vertical, nb_tags, tags):
    self.id = identifier
    self.is_vertical = is_vertical
    self.tags = tags
    self.nb_tags = len(tags)

  def __repr__(self):
        return " ID : " + str(self.id) + " is vertical : " + str(self.is_vertical) +" nbtags : " + str(self.nb_tags) + " tags :  "+ " ".join(self.tags)  +"\n"


  def calculate_point(self, other_photo):
    return min(
      len(self.common_tags(other_photo)),
      len(self.tags_not_in_other(other_photo)),
      len(self.other_tags_not_in_ours(other_photo))
    ) 
  
  def common_tags(self, other_photo):
    tags = set()
    for tag in other_photo.tags:
      if tag in self.tags:
        tags.add(tag)
    return tags
  
  def tags_not_in_other(self, other_photo):
    tags = set()
    for tag in self.tags:
      if tag not in other_photo.tags:
        tags.add(tag)
    return tags
  
  def other_tags_not_in_ours(self, other_photo):
    tags = set()
    for tag in other_photo.tags:
      if tag not in self.tags:
        tags.add(tag)
    return tags
