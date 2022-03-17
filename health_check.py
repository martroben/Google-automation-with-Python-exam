#!/usr/bin/env python3

import shutil
import psutil
import socket
import smtplib
import time
import emails

# Inputs

# CPU usage > cpu %
# free disk space < diskspace %
# available memory < memory MB
# localhost resolves to localhost ip
thresholds = {
  "cpu": 80,
  "diskspace": 20,
  "memory": 500,
  "localhost": "127.0.0.1"}

interval = 60
username = "student"
mail_server_ip = "localhost"

error_messages = {
  "cpu": "Error - CPU usage is over {}%".format(thresholds["cpu"]),
  "diskspace": "Error - Available disk space is less than {}%".format(thresholds["diskspace"]),
  "memory": "Error - Available memory is less than {}MB".format(thresholds["memory"]),
  "localhost": "Error - localhost cannot be resolved to {}".format(thresholds["localhost"])}

# Create the e-mail server connection
mail_server = smtplib.SMTP(mail_server_ip)


def get_failing_item(state):
  """Return name of failing item or None if none are failing"""
  for key, value in state.items():
    if not value:
      return key
  return None


while True:
    
  # Monitor system state
  failing_item = None
  while failing_item == None:
    time.sleep(interval)
    system_state = {
      "cpu": psutil.cpu_percent() < thresholds["cpu"],
      "diskspace": shutil.disk_usage("/").free / shutil.disk_usage("/").total * 100 > thresholds["diskspace"],
      "memory": psutil.virtual_memory().free / 2**10 / 2**10 > thresholds["memory"],
      "localhost": socket.gethostbyname("localhost") == thresholds["localhost"]}
  
    failing_item = get_failing_item(system_state)
  
  # Send e-mail alert if something fails
  error_msg = error_messages[failing_item]
  
  email_msg = emails.generate_email(
    sender="automation@example.com",
    recipient=username + "@example.com",
    subject=error_msg,
    body="Please check your system and resolve the issue as soon as possible.")
  
  emails.send_email(
    mail_serv=mail_server,
    email = email_msg)
