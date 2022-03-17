#! /usr/bin/env python3

import os
import requests
import re

# Inputs
descriptions_dir = "/home/student/supplier-data/descriptions/"
upload_url = "http://xxx.xxx.xxx.xxx/fruits/"

# Get list of all .txt files in folder
file_list = os.listdir(descriptions_dir)
txt_paths = [descriptions_dir + item for item in file_list if bool(re.search(r"txt", item))]

# Create a json post request from info in the .txt files
# Upload descriptions to web service
for txt_file in txt_paths:
  with open(txt_file) as in_file:
    content_list = in_file.readlines()
    content_dir = {
      "name": content_list[0].replace("\n", ""),
      "weight": int(content_list[1].replace("lbs\n", "")),
      "description": content_list[2].replace("\n", ""),
      "image_name": os.path.basename(txt_file).replace("txt", "jpeg")}
    
    response = requests.post(upload_url, json=content_dir)
    print(response.status_code)
