import os
from parser import parser

DATASET_PATH = os.path.join(os.getcwd(), 'dataset')

for file_path in os.listdir(DATASET_PATH):
  with open(os.path.join(DATASET_PATH, file_path)) as f:
    lines = f.readlines()
    photos = parser(lines)
    print(photos)
  
  # For testing only, breaks the loop
  break
