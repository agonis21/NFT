import smtplib, os


EMAIL_ADDRESS = os.environ.get("semonynyc@gmail.com")
EMAIL_PASSWORD = os.environ.get("Gm32VCUMp5youtube")
#EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
#EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = "Price Update for WGG#360"
    body = "WGG#360 has an offer for  1.23 ETH"

    msg = f'Subject: {subject}\n\n{body}'
    smtp.sendmail(EMAIL_ADDRESS, "asmgoni@protonmail.com", msg)
