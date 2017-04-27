import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = "noreply.snitchalarm@gmail.com"
toaddr = "jeremy.jodi168@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Door has been opened"

body = "Not You? Contact your neighbours or the local security."
msg.attach(MIMEText(body, 'plain'))

name ="Snitch"
open = 0
print("Hello " + name)

print("Door is open")
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
print("ok")
server.login(fromaddr, "magnet123")
print("2")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
open = 1
