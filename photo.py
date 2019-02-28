class Photo:
  def __init__(self, is_vertical, tags):
    self.is_vertical = is_vertical
    self.tags = tags
    self.nb_tags = len(tags)
