import os
from email.message import EmailMessage
import mimetypes

def generate_email(**kwargs):
  """Generate an e-mail object from inputs"""
  message = EmailMessage()

  required_inputs = ["sender", "recipient", "subject", "body"]
  for name in required_inputs:
    if name not in kwargs:
      sys.exit("Required input argument '{}' not supplied".format(name))

  # Set headers
  message["From"] = kwargs["sender"]
  message["To"] = kwargs["recipient"]
  message["Subject"] = kwargs["subject"]

  # Set body
  message.set_content(kwargs["body"])

  # Add attachment (if included in input)
  if "attachment" in kwargs:
    mime_type, _ = mimetypes.guess_type(kwargs["attachment"])
    mime_type, mime_subtype = mime_type.split("/", 1)

    with open(kwargs["attachment"], "rb") as pdf_report:
      message.add_attachment(
        pdf_report.read(),
          maintype=mime_type,
          subtype=mime_subtype,
          filename=os.path.basename(kwargs["attachment"]))

  return message


def send_email(mail_serv, email):
  """Sends e-mail by mail server specified in the input"""
  undelivered = mail_serv.send_message(email)
  
  if len(undelivered) > 0:
    return "Undelivered recipients: {}".format(str(undelivered))
  else:
    return "All e-mails delivered successfully"
