#!/usr/bin/env python3

import os
from datetime import date
import reports
import re
import getpass
import smtplib
import emails

# Inputs
descriptions_dir = "/home/student/supplier-data/descriptions/"
username = "student"
pdf_path = "/tmp/processed.pdf"
mail_server_ip = "localhost"

# Get current date for pdf title
date_string = date.today().strftime("%d-%m-%Y")
date_line = "Processed update on {}".format(date_string)

# Get description file paths
file_list = os.listdir(descriptions_dir)
txt_paths = [descriptions_dir + item for item in file_list if bool(re.search(r"txt", item))]

# Generate pdf content
paragraph_string = ""
for txt_file in txt_paths:
  with open(txt_file) as in_file:
    content_list = in_file.readlines()
    paragraph_string += "name: {}<br/>weight: {}<br/><br/>".format(content_list[0].replace("\n", ""), content_list[1].replace("\n", ""))

                                                                                                                              
if __name__ == "__main__":

  reports.generate_report(pdf_path, date_line, paragraph_string)
  email_msg = emails.generate_email(
    sender="automation@example.com",
    recipient=username + "@example.com",
    subject="Upload Completed - Online Fruit Store",
    body="All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
    attachment=pdf_path)

  mail_server = smtplib.SMTP(mail_server_ip)
  emails.send_email(
    mail_serv=mail_server,
    email=email_msg)
  mail_server.quit()
