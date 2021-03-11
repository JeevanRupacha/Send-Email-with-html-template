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
    msg = EmailMessage()


    def __init__(self,email,email_pass,sendToEmail):
        self.email = email
        self.email_pass = email_pass
        self.sendToEmail = sendToEmail
    

    ### send birthday email 
    def sendBirthdayEmail(self):
        email_tamplate = """
        <!DOCTYPE html>
        <html>
            <body>
                <h1 style="color:#F1239F; margin: 0px auto">Happy Birthday!</h1>
                <h3 style="color:#F39912"> Dear Grishmin,</h3>
                <p> I met lots of people in my life but very few like you.
                 You are the amazing man I ever met in my life . I wish happy 3th day and many many wishes more.
                I know its not the right time of your birthday but I gave you in advanced. Just kidding I am testing the auto email service and this is auto sended email.
                If u get this emamil than You can give me feedback . Ok

                
                </p>

                <img style="width:100%" src = "https://firebasestorage.googleapis.com/v0/b/whats-app-clone-d85bd.appspot.com/o/birthdaycard2.jpg?alt=media&token=286fb09d-6630-4902-baad-200454ec9c89"></img>
                <h3 style="color:#F39912"> Jeevan Rupacha </h3>
            </body>
        </html>
        """

        self.msg['subject'] = 'Happy Birthday to You '
        self.msg['from'] = self.email
        self.msg['to'] = self.sendToEmail
        self.msg.set_content = " "
        self.msg.add_alternative(email_tamplate, subtype = "html")


        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(self.email, self.email_pass)
                smtp.send_message(self.msg)
                print("email send Successfully !")
        except Exception as e:
            print("error occured here " + str(e))



emailService = EmailService('rupachasgvn@gmail.com','rupachazevn', 'ruupachagvn@gmail.com')
emailService.sendBirthdayEmail()
