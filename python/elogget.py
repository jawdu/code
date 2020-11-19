#! /usr/bin/env python3

# put together as a favour for someone to automate a task
# sources: https://stackoverflow.com/a/59650691 https://stackoverflow.com/a/22857102

# no arguments when called:
# - checks the outlook for unread emails
# - downloads any attachments (png, jpg, jpeg, gif) into 'outputdir'
# - marks emails as read.
# - write sender, subject, filename to info.tmp
# arguments:
# - reply sender
# - if you get Exception:OutboundSpamException when sending, then you'll need to log into outlook
#   and verify your account

import imaplib
import email
import os
import sys
import smtplib, ssl

server = 'SERVER NAME'
user = 'USER NAME'
password = 'PASSWORD'
outputdir = 'new/'  # where to put downloaded files

# connects to email client through IMAP
def connect(server, user, password):
    m = imaplib.IMAP4_SSL(server)
    m.login(user, password)
    m.select()
    return m

# downloads attachment for an email id, which is a unique identifier for an
# email, which is obtained through the msg object in imaplib, see below 
# subjectQuery function. 'emailid' is a variable in the msg object class.

def dlAttachmentsInEmail(m, emailid, outputdir):
    resp, data = m.fetch(emailid, "(BODY.PEEK[])")
    email_body = data[0][1]
    mail = email.message_from_bytes(email_body)
    if mail.get_content_maintype() != 'multipart':
        return
    for part in mail.walk():
        if part.get_content_maintype() != 'multipart' and part.get('Content-Disposition') is not None:
            if os.path.splitext(part.get_filename())[1] in {".png", ".jpg", ".jpeg", ".bmp", ".gif"}:
                open(outputdir + part.get_filename(), 'wb').write(part.get_payload(decode=True))
                # write sender, subject, filename to file, info.tmp is created and deleted in elloget.sh
                f = open("info.tmp", "a")
                f.write(mail.get('From') + "\n")
                f.write(mail.get('Subject') + "\n")
                f.write(part.get_filename() + "\n")
                f.close

# download attachments from all unread emails

def emailQuery():
    m = connect(server, user, password)
    m.select("Inbox")
    typ, msgs = m.search(None, '(UNSEEN)')    
    msgs = msgs[0].split()
    for emailid in msgs:
        dlAttachmentsInEmail(m, emailid, outputdir)
        # Mark them as seen
        m.store(emailid, '+FLAGS', '\Seen')

# get info for confirmation reply email

def getInfo(imgFile):
    with open("info.tmp") as f:
        for n, line in enumerate(f):
            if imgFile in line:
                num = n
                break
    with open("info.tmp") as f:
        for n, line in enumerate(f):
            if n == num-2:
                senderRaw = line
            if n == num-1:
                subject = line
                break
    sender = senderRaw.split('<', 1)[1].split('>')[0]
    name = senderRaw.split(' <')[0]
    
    return sender, subject, name

def emailReply(newId, imgFile, sender, subject, name):
    # send replies to whoever has submitted an image uploaded to elogger
    port = 587  # For starttls
    smtp_server = "SMTP.SERVER"

    subject = "Re: " + subject + " - success with newID " + newId
    text = "Hi " + name + ", your file " + imgFile + " has been uploaded to elog with ID = " + newId
    message = 'Subject: {}\nTo: {}\nFrom: {}\n\n{}'.format(subject, sender, user, text)

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as nserver:
        nserver.starttls(context=context)
        nserver.login(user, password)
        nserver.sendmail(user, sender, message)

if len(sys.argv) == 1:
    # if no args, check outlook for new emails
    emailQuery()
else:
    # if args, send confirmation emails
    newId = sys.argv[1]
    imgFile = sys.argv[2].split('/')[1]         # strip path from imgFile
    sender, subject, name = getInfo(imgFile)
    emailReply(newId, imgFile, sender, subject, name)


