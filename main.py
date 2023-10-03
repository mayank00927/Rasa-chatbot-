import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("mak008.ms@gmail.com", "iszr ydvq sykl wfqw")

# message to be sent
message = "Message_you_need_to_send"

# sending the mail
s.sendmail("mak008.ms@gmail.com", "jobs.mayank00927@gmail.com", message)

# terminating the session
s.quit()
