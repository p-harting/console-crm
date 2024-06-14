import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class MailManager:
    def send_mail(self, receiver_mail, subject, message, password):
        """
        Sends an email using SMTP protocol to the specified receiver address.

        :param receiver_mail: The email address of the recipient.
        :param subject: The subject line of the email.
        :param message: The body content of the email.
        :param password: The password for the sender's email account.
        """
        from_address = "console.crm.sender@gmail.com"

        msg = MIMEMultipart()
        msg['From'] = from_address
        msg['To'] = receiver_mail
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain', 'utf-8'))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_address, password)

        server.send_message(msg)
        server.quit()
