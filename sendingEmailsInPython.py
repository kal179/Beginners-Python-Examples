import smtplib

# REMEMBER : dont send mails through public computers or servers 

# connecting to googles serevrs
serverToLogin = smtplib.SMTP('smtp.gmail.com' , 587)
# Username
userName = str(input('Username for Gmail : '))
# password
password = str(input('Password Of Account : '))
# Logging in 
serverToLogin.login(userName , password)

def sendMail():
	yourEmail = str(input('Your Email Address : ')) # senders email address
	toSendEmail = str(input('Receivers Email Address')) # receivers email address
	messageHead = str(input('Message Head : ')) # Message head
	messageBody = str(input('Message : ')) # main message
	fullMessage = messageHead + '\n' + messageBody # full message
	serverToLogin.sendmail(yourEmail , toSendEmail , fullMessage)  # sending email address through server 

while True:
	toSendOrNot = str(input('Send or End : '))
	if toSendOrNot == 'Send':
		print('\n')
		print(sendMail())
	else :
		quit()




