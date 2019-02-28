class Photo:
  def __init__(self, is_vertical, nb_tags, tags):
    self.is_vertical = is_vertical
    self.tags = tags
    self.nb_tags = nb_tags

  def __repr__(self):
    return "is vertical : " + str(self.is_vertical) +" nbtags : " + self.nb_tags + " tags : ".join(self.tags)  
