import os
from Parser import parser
from generate_slides import generate_slides_from_photos

DATASET_PATH = os.path.join(os.getcwd(), 'dataset')

for file_path in os.listdir(DATASET_PATH):
  dataset_file_path = os.path.join(DATASET_PATH, file_path)
  photos = parser(dataset_file_path)
  slides = generate_slides_from_photos(photos)

  sorted(photos, key=lambda s: len(s.tags),reverse=True)

  print(photos)

  # For testing only, breaks the loop
  break
