from dotenv import load_dotenv
import os
import yagmail

# Load environment variables from .env
load_dotenv()

sender=os.getenv("SENDER")
receiver=os.getenv("RECEIVER")
password=os.getenv("PASSWORD")
subject="Email sent using Python"
contents="Hey!\nThis is an email sent from stock price notifier.\nI intend to develop a project where you get this email whenever the stocks you have bought have a change more than 2%"

yag = yagmail.SMTP(user=sender, password=password)
yag.send(to=receiver, subject=subject, contents=contents)
print("The email has been sent.")