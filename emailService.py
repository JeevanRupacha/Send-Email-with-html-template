from email.message import EmailMessage
import smtplib

### Construcor takes three paramenters 
### email = your email to send mail
### email_pass = your email password 
### sendToEmail = email to whom send the emial

class EmailService :
    email = ''
    email_pass = ''
    sendToEmail = ''
    html_template = ''
    msg = EmailMessage()


    def __init__(self,email,email_pass,sendToEmail):
        self.email = email
        self.email_pass = email_pass
        self.sendToEmail = sendToEmail

    def set_hmtl_template(self, html_template):
        self.html_template = html_template
    

    ### send birthday email 
    def sendBirthdayEmail(self):
        html_tamplate = self.hmtl_template
        

        self.msg['subject'] = 'Happy Birthday to You '
        self.msg['from'] = self.email
        self.msg['to'] = self.sendToEmail
        self.msg.set_content = " "
        self.msg.add_alternative(html_tamplate, subtype = "html")


        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(self.email, self.email_pass)
                smtp.send_message(self.msg)
                print("email send Successfully !")
        except Exception as e:
            print("error occured here " + str(e))


