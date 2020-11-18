#! /usr/bin/env python3

# put together as a favour for someone to automate a task
# sources: https://stackoverflow.com/a/59650691 https://stackoverflow.com/a/22857102

# - checks the outlook for unread emails
# - downloads any attachments (png, jpg, jpeg, gif) into 'outputdir'
# - marks emails as read.
# - write sender, subject, filename to info.txt for use with elog in shell script


import imaplib
import email
import os

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
                # write sender, subject, filename to file, info.txt is created and deleted in elloget.sh
                f = open("info.txt", "a")
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

emailQuery()

