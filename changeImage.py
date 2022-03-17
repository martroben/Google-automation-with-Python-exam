#!/usr/bin/env python3

import os
import re
from PIL import Image

# Inputs
images_dir = "/home/student/supplier-data/images/"

# Get a list of paths of all .tiff files in directory
file_list = os.listdir(images_dir)
tiff_files = [item for item in file_list if bool(re.search(r"tiff", item))]
tiff_paths = [images_dir + filename for filename in tiff_files]

# Convert each image to 600x400 jpeg
for path in tiff_paths:
  image_in = Image.open(path)
  image_out = image_in.resize((600,400)).convert("RGB")

  out_path = re.sub(r".tiff", ".jpeg", path)
  print(out_path)
  image_out.save(out_path)
