import smtplib

class MailManager:
    def send_mail(self, receiver_mail, subject, message, password):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        text = f"Subject: {subject}\n\n{message}"
        server.login("console.crm.sender@gmail.com", password)
        server.sendmail("console.crm.sender@gmail.com", receiver_mail, text)
