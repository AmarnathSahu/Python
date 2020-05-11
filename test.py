import json 
import csv
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

jsonObject = {}
def send_mail(send_from, send_to, subject, text, files=None,
              server="smtp.gmail.com:587"):
    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)

    smtp = smtplib.SMTP(server)
    smtp.starttls()
    smtp.login('Email_Id','Password')
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()


with open('data2.json', 'r') as file:
    array = file.read().replace('\n', '')
	

x = array
y = '';
mainList = []
res = [i for i in range(len(x)) if x.startswith('{', i)]
for i in range(len(res)):
  initial = res[i]
  if(i == len(res)-1):
    final = len(x)
  else:
    final = res[i+1]
  y = x[initial:final].strip()
  mainList.append(y)

data_file = open('data_file1.csv', 'w') 

csv_writer = csv.writer(data_file)

count = 0
for dataItem in mainList:
	dataItem = json.loads(dataItem)
	if count == 0:
		header = dataItem.keys()
		csv_writer.writerow(header)
		count += 1 
	
	csv_writer.writerow(dataItem.values()) 

#data_file = open('data_file1.csv', 'r')
send_mail('amarnathsahu78@gmail.com',['amarnathsahu78@gmail.com'], 'testMail', 'Hello', ['data_file1.csv']) 
data_file.close() 
    
