# Adding attachments using email package

import smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendMail(gmailId, password):
    """
    senderEmail = ""
    password = input('Enter your password : ')
    receiverEmail = ""
    """
    senderEmail = gmailId
    receiverEmail = gmailId

    subject = "Job Updates"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = senderEmail
    message["To"] = receiverEmail
    message["Subject"] = subject
    message["Bcc"] = receiverEmail

    # Create the plain-text or HTML version of your message
    '''
    text = """\
    Hi,
    How are you?
    We have found some Job profiles matching your skills, please find them in the below attached file...
    
    All The Best...
    :) :) :)
    """
    '''

    html = """\
    <html>
        <body>
            <p>Hi, <br>
                How are you? <br>
                We have found some Job profiles matching your skills, please find them in the below attached file... <br>
                <br>
                All The Best....<br>
                :) :) :) <br>
            </p>
        </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    #part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    #message.attach(part1)
    message.attach(part2)

    # Attach The .txt file
    filename = "Posts/Jobs_Details.txt"

    # Open txt file in binary mode
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename = {filename}",
    )


    message.attach(part)
    text = message.as_string()

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(senderEmail, password)
        server.sendmail(senderEmail, receiverEmail, text)
        print("Email Sent...... :)")
