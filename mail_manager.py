import smtplib


class MailManager:
    def send_mail(self, receiver_mail, subject, message, password):
        """
        Sends an email using SMTP protocol to the specified receiver address.

        :param receiver_mail: The email address of the recipient.
        :param subject: The subject line of the email.
        :param message: The body content of the email.
        :param password: The password for the sender's email account.
        """
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        text = f"Subject: {subject}\n\n{message}"
        server.login("console.crm.sender@gmail.com", password)
        server.sendmail("console.crm.sender@gmail.com", receiver_mail, text)
        server.quit()
