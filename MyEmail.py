from emailService import EmailService
my_html_template = """
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

emailService = EmailService('..n@gmail.com','password', '...@gmail.com')
emailService.set_html_template(my_html_template)
emailService.sendBirthdayEmail()