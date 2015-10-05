#!/usr/bin/python
import smtplib as mail
mailserver = mail.SMTP("example.net")
mailserver.login("Testusr","testpassword")
msg = '''From: SenderNAme <sender@null.org>
To: <receipient@null.org>
Subject: A Test email Message!
Contnet-type: text/html
MIME-Version: 1.0

This will be the body of your email.'''
mailserver.sendmail("sender@example.net", "receipient@example.net", msg)