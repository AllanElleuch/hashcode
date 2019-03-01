import os
from Parser import parser
from generate_slides import generate_slides_from_photos
from order_slides import order_slides
from output import output

DATASET_PATH = os.path.join(os.getcwd(), 'dataset')

def run(is_release=False):
  files = os.listdir(DATASET_PATH)

  if not is_release:
    files = files[1:2]

  for file_path in files:
    print('File:', file_path)
    dataset_file_path = os.path.join(DATASET_PATH, file_path)
    output_file_path = os.path.join(DATASET_PATH, '..', 'out', file_path)
    photos = parser(dataset_file_path)
    slides = generate_slides_from_photos(photos)

    slides = order_slides(slides)
    output(slides, output_file_path)
