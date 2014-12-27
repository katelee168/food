
def send_email(recipient, text, html):
	import smtplib
	import account
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText

	# me == my email address
	# recipient == recipient's email address
	me = "dining.princeton@gmail.com"

	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "This is a subject"
	msg['From'] = me
	msg['To'] = me
	msg['BCC'] = ", ".join(recipient)

	# Record the MIME types of both parts - text/plain and text/html.
	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')

	# Attach parts into message container.
	# According to RFC 2046, the last part of a multipart message, in this case
	# the HTML message, is best and preferred.
	msg.attach(part1)
	msg.attach(part2)

	# Send the message via local SMTP server.
	# sendmail function takes 3 arguments: sender's address, recipient's address
	# and message to send - here it is sent as one string.
	try: 
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		server.login(account.login,account.password)
		problems = server.sendmail(me, recipient, msg.as_string())
		server.close()
		print 'sucessfuly sent mail'
	except:
		print 'failed to send mail'