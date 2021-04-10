import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
#from whatsappMessage import Age
#print("RUNNING...")
sender_email = "kayabacryptobot@gmail.com"
receiver_email = "jdavidgomezca@gmail.com"
password = "Sara2019"

info = ('0xfd640bdb374729fe78d24bbe4e5b8faf83ae2ed5', 1274002.59, '0xb47f4ed276325ce0b7798bc6a8121ee46ea43a8c634b8920c5b8ecfca8cb9523', 'SELL', 21114296.98, 'HOGL Finance', '0x182c763a4b2fbd18c9b5f2d18102a0ddd9d5df26', 897.16, 0.0, datetime.datetime(2021, 4, 10, 11, 52, 32))


def SendEmail(info):

    Address = info[0]
    Total_Balance = "{:,}".format(info[1]) 
    Hash = info[2] 
    Action = info[3]
    if Action == "SELL":
        Action = "SOLD"
    else:
        Action == "BOUGHT"
    Aumount = info[4]
    Token = info[5]
    TokenContract = info[6]  
    DOLLARS = "{:,}".format(info[7])
    Invested = info[8] 
    Age = info[9]

    message = MIMEMultipart("alternative")
    message["Subject"] = "Whale:  ${Balance}  --{action}--  {Token}  for  ${Dolars}    at {time}".format(Balance=Total_Balance, action=Action, Token=Token, Dolars=DOLLARS, time=Age)
    message["From"] = sender_email
    message["To"] = receiver_email

    Whale = "https://bscscan.com/address/" +str(Address)
    Transaction = "https://bscscan.com/tx/" + str(Hash)
    TContract = "https://bscscan.com/token/" + str(TokenContract)
    Chart = "https://poocoin.app/tokens/" + str(TokenContract)
    # Create the plain-text and HTML version of your message
    text = """\
    Whale Account Overview:
    {whale}\n
    Transaction Receipt:
    {transaction}\n
    Token Contract:
    {TC}\n
    Percentage of account Used:
    {per}\n
    {tk} Chart:
    {chart}\n

    With love,
    Kayaba Crypto Bot""".format(whale=Whale,
                                transaction=Transaction,
                                TC=TContract,
                                per=Invested,
                                tk = Token,
                                chart=Chart)


    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)


    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
if info[1] > 1000000:
    SendEmail(info)
    print("done")
