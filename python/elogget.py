#! /usr/bin/python3

# put together as a favour for someone to automate a task
# sources: https://stackoverflow.com/a/59650691 https://stackoverflow.com/a/22857102

# - checks unmonitored outlook address for unread emails
# - downloads any attachments (png, jpg, jpeg, gif) into 'outputdir'
# - marks emails as read.


import imaplib
import email
import os

server = 'SERVER NAME'
user = 'USER NAME'
password = 'PASSWORD'
outputdir = 'attachments'  # if you want to use pwd, remove the '/' in the open(outputdir + '/' + ... below)

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
                open(outputdir + '/' + part.get_filename(), 'wb').write(part.get_payload(decode=True))

# download attachments from all emails with a specified subject line
# as touched upon above, a search query is executed with a subject filter,
# a list of msg objects are returned in msgs, and then looped through to 
# obtain the emailid variable, which is then passed through to the above 
# dlAttachmentsinEmail function

def subjectQuery(subject):
    m = connect(server, user, password)
    m.select("Inbox")
    #typ, msgs = m.search(None, '(SUBJECT "' + subject + '")')
    typ, msgs = m.search(None, '(UNSEEN)')    
    msgs = msgs[0].split()
    for emailid in msgs:
        dlAttachmentsInEmail(m, emailid, outputdir)
        # Mark them as seen
        m.store(emailid, '+FLAGS', '\Seen')

subjectQuery(subject)



