#!/usr/bin/env python3

import os
import re
import requests

# Inputs
images_dir = "/home/student/supplier-data/images/"
upload_url = "http://xxx.xxx.xxx.xxx/upload/"

# Get a list of paths of all .jpeg files in directory
file_list = os.listdir(images_dir)
jpeg_paths = [images_dir + item for item in file_list if bool(re.search(r"jpeg", item))]

# Post all .jpeg files to a web service
for path in jpeg_paths:
  with open(path, "rb") as image:
    response = requests.post(upload_url, files={"file": image})
    print(response.status_code)
