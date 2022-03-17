from datetime import date
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, paragraph):
  """Generates .pdf file with supplied title and body (paragraph)
     Saves to supplied path (attachment)"""
  report = SimpleDocTemplate(attachment)
  styles = getSampleStyleSheet()

  report_title = Paragraph(title, styles["h1"])
  report_body = Paragraph(paragraph)
  report.build([report_title, Spacer(1, 0), report_body])
