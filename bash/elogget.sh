#!/bin/bash

# confirmed works for more than 1 new email, and emails with more than 1 attachment
# setup to work only if run in directory with elogget.py and elogget.sh, *and* with a folder new/
# on first run through, it calls elloget with no arguments, which means it checks for new emails
# any new emails with (png, jpg, jpeg, bmp, gif) attachments are marked as read, and images downloaded
# into new/, and details are written to info.tmp.
# then, for every file in new/, upload to elog. on receipt of an ID, the filename and ID will be arguments
# for elogget.py, which will send email confirmation. it will grab email for each filename from info.tmp
# afterwards, all files and info.tmp are deleted.

touch info.tmp

./elogget.py # no arguments -> check for new emails

if [ -n "$(ls -A new/ 2>/dev/null)" ]; then
    # if new files downloaded
    for filename in new/*.*; do
        # filename will be new/filename.ext
        # .\elog.exe $filename
        # when we get back id from elog, also if you want to write a log do it now in case outlook is a git next step
        id=7 #dummy id
        ./elogget.py $id $filename # arguments -> send confirmation emails
        rm $filename
    done
fi

rm info.tmp

