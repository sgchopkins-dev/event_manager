import logging
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


from rfc5424logging import Rfc5424SysLogHandler
NAS = os.getenv('NAS')
EMAIL_USERNAME = os.getenv('EMAIL_USERNAME')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_SERVER = os.getenv('EMAIL_SERVER')    

logger = logging.getLogger("email")
logger.setLevel(logging.INFO)

handler = Rfc5424SysLogHandler(address=(NAS, 514))
logger.addHandler(handler)


def email_events(recipients, events):
    for address in recipients:
        message = MIMEMultipart("related")
        message["Subject"] = "Event Manager Daily Report"
        message["From"] = EMAIL_USERNAME
        message["To"] = address
        html = """\
            <html>
              <head></head>
              <body>
                <p>Upcoming Events<br>
                   {0}

                   Regards,

                   Python-Bot 2.0
                </p>
              </body>
            </html>

            """.format(events)
        partHTML = MIMEText(html, "html")
        message.attach(partHTML)
        msg_body = message.as_string()
        server = smtplib.SMTP(EMAIL_SERVER, port="587")
        server.ehlo()  # send the extended hello to our server
        server.starttls()  # tell server we want to communicate with TLS encryption
        resp_code, response = server.login(
            message["From"], EMAIL_PASSWORD
        )  # login to our email server
        server.sendmail(message["From"], message["To"], msg_body)
        logger.info(f"events email sent to: {address}")
