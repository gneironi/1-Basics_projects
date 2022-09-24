##This excersice is about use an SMTP server.
#In this case I'm using: https://app.sendinblue.com/

#TODO: make a funtion than can sen a mail by smtp


import smtplib
from dotenv import load_dotenv
import os
load_dotenv()

mail_account = os.getenv("MAIL_ACCOUNT")
mail_pass = os.getenv("MAIL_PASS")

def automatic_email():
   user = input("Enter your Name >>: ")
   email = input("Enter your email address >>: ")
   message = (f"Dear {user}, Welcome to my Github")
   s = smtplib.SMTP('smtp-relay.sendinblue.com', 587 )
   s.starttls()
   s.login(mail_account, mail_pass)
   s.sendmail(mail_account, email,message)
   print("Email Sent successfully")

automatic_email()


#used tools:
#.dotenv (to set environment variables),
#.gitignore (to hide .env file),
# os library (to get de environment variables), 
# smtplib (to send teh mail)


