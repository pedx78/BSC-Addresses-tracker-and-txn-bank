import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import webbrowser
import requests
from urllib.request import Request, urlopen
#from whatsappMessage import Age
#print("RUNNING...")
sender_email = "kayabacryptobot@gmail.com"
receiver_email = "jdavidgomezca@gmail.com"
password = "Sara2019"

#info = ('0xfd640bdb374729fe78d24bbe4e5b8faf83ae2ed5', 1274002.59, '0xb47f4ed276325ce0b7798bc6a8121ee46ea43a8c634b8920c5b8ecfca8cb9523', 'SELL', 21114296.98, 'HOGL Finance', '0x182c763a4b2fbd18c9b5f2d18102a0ddd9d5df26', 897.16, 0.0, datetime.datetime(2021, 4, 10, 11, 52, 32))

def Pumps_Addresses():
    solution =  ['0x3fb7b0eed0efda15760f81f356f90d20de40b59f',
    '0xb0f50b8a1c3f7a8f6f3085c1df7b28663f4889f6',
    '0xa129161965dcf2f1c1e72cf81b794fababb775f6',
    '0xc126a5b653e48f3a7c9cf000a3b795dd94a11d30',
    '0xa129161965dcf2f1c1e72cf81b794fababb775f6',
    '0xb82e44ebdc162cf892c2bfaf2a8a4fe7b126f9e9',
    '0xc126a5b653e48f3a7c9cf000a3b795dd94a11d30',
    '0x074811b45242a8471885a31ff92afc768aea4903',
    '0x8aa7de2ce13756f214a54c061958a2aca7685f5b']
    
    return solution

#print(Pumps_Addresses())
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
    if info[7] == None:
        DOLLARS = "unknown"
    
    if info[7] != None:
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

    # Telegram bot logic
    
    pump_keys = Pumps_Addresses()

    pump_dict = {'0x3fb7b0eed0efda15760f81f356f90d20de40b59f':'BOSSMAN%20WALLET%20-ORIGINAL-',
        '0xb0f50b8a1c3f7a8f6f3085c1df7b28663f4889f6':'Shit Coin Pump Wallet 1',
        '0xa129161965dcf2f1c1e72cf81b794fababb775f6':'Shit Coin Pump Wallet 2',
        '0xc126a5b653e48f3a7c9cf000a3b795dd94a11d30': 'Wallet that tests to see honey pot before pump',
        '0xa129161965dcf2f1c1e72cf81b794fababb775f6': 'Shitcoin pump wallet 3',
        '0xb82e44ebdc162cf892c2bfaf2a8a4fe7b126f9e9': 'Other Pump wallet 1',
        '0xc126a5b653e48f3a7c9cf000a3b795dd94a11d30': 'Other Pump wallet 2',
        '0x074811b45242a8471885a31ff92afc768aea4903': 'Other Pump wallet 3',
        '0x8aa7de2ce13756f214a54c061958a2aca7685f5b': 'Other Pump wallet 4'}

    # Iteriate the pump_keys array and send message if the address is in it 
    for i in pump_keys:
        if i == Address:
            # set the name with the name assocciated with the key in pump_dict
            pump_name = pump_dict[i]
            # Eliminate spaces in the token name and account name
            pump_name = pump_name.translate(str.maketrans({' ': '%20', ')': ''}))
            Token = Token.translate(str.maketrans({' ': '%20', ')': ''}))
            # Build telegram message
            Telegram_Message = "https://api.telegram.org/bot1733010924:AAEJUQSQ9y3b0C0qH2EmzM4sKpp_wUl40jc/sendMessage?chat_id=-1001265752428&text=Kayaba%20Crypto%20Bot%0A%0A--TRANSACTION%20ALERT!!!--%0A%0A---{name}%20{action}---%0A%0A%0AToken:%20%20{Token}%20For%20${value}%0A%0ATransaction%20Receipt:{transaction}%0AToken%20Contract:{TC}%0A{Token}%20Chart:{chart}%0A%0A%20Any%20Donations%20are%20welcome%20:)%20%20--0xd4ec9a0BCd9D1Aeb295c0412641d15095A0C002F--".format(name=pump_name,action=Action,Token = Token, value = DOLLARS,transaction=Transaction,TC=TContract,chart=Chart)
            #webbrowser.open(Telegram_Message, new=2)
            # Use credentials and send message
            headers = {'User-Agent': 'XYZ/3.0'}
            req = Request(Telegram_Message , headers=headers) 
            run_message = urlopen(req).read()


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

    '''
if info[1] > 1000000:
    SendEmail(info)
    print("Email Sent")
    '''
