#pip install psutil
import psutil

#email Stuff
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

USER = "user"


def is_user_logged_in(username):
    for user in psutil.users():
        if user.name == username:
            return True
    return False

if __name__ == "__main__":
    username = USER
    if is_user_logged_in(username):
        print(f"{username} is logged in.")
    else:
        print(f"{username} is not logged in.")

        #email if arcgis user is not logged in

        TO = ["user@email.com"]
        FROM = "user@email.com"

        SUBJECT = f"{username} user not logged in on Serer"

        TEXT = f"{username} user not logged in on Server</br></br>" 
        
        BODY = "\r\n".join((
                "From: %s" % FROM,
                "To: %s" % TO,
                "Subject: %s" % SUBJECT ,
                "MIME-Version: 1.0",
                "Content-type: text/html",
                TEXT
                ))
        server = smtplib.SMTP('############')
        server.sendmail(FROM, TO, BODY)
        server.quit()
