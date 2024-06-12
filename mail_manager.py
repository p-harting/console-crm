import smtplib

class MailManager:
    def send_mail(self, receiver_mail, subject, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
