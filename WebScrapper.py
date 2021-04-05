from pandas.core.dtypes.missing import notnull
import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
#https://bscscan.com/address/0xcC64ea842FcDe4283CF239259f7462Ef809c44FD
import webbrowser
def getTokenBalance(whale):
    url = "https://bscscan.com/address/" + whale
    #print(url)
  
    '''
    url = "https://bscscan.com/address/" + whale
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    getId = soup.find(id='availableBalanceDropdown')
    results = getId.text
    '''
    req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    

    soup = BeautifulSoup(page, 'html.parser')
    #print(soup)
    getId = soup.find(id='availableBalanceDropdown')
    #print(type(getId))
    results = getId.text

    extra = getId.find_all('span', class_='badge badge-primary mx-1')
    #print("NEXT")
    done = extra[0].text

    #print(results)
    final = results.replace(done, '')
    #print(final)
    final = final.replace('\n', '')
    #print(final)
    final = final.replace('$', '')
    #print(final)
    final = final.replace(',', '')
    final = float(final)
    #print(type(final))
    #webbrowser.open(url, new=2)
    return final



#print(getTokenBalance("0x0c8c62a7f883c6e47c8c5790474d4eb8a48924f2"))




def getTxnValue(hash, action):
    responseArray = []
    value = 0
    url = "https://bscscan.com/tx/" + hash
    #webbrowser.open(url, new=2)

    #page = requests.get(url)

    req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    
    soup = BeautifulSoup(page, 'html.parser')
    #getId = soup.find(id='availableBalanceDropdown')
    #results = getId.text

    results = soup.find_all('span', class_='mr-1')
    #results1 = results.find_all(attrs={"data-toggle": "tooltip"})
    #print("NEXT")
    #done = extra[0].text
    #print(results)
    index = 0
    #print("HELLO")
    for result in results:
        #print("run")
        a = results[index].find_all(attrs={"data-toggle": "tooltip"})
        index += 1
        #print(result)
        #print("Solution: ---------------------------")
        if a != []:
            #print(type(a))
            #print(a[0].text)
            #print(type(a[0].text))
            responseArray.append(a[0].text)
            #print(responseArray)
    if len(responseArray) > 1:
        if action == "BUY":
            value = responseArray[1]
            value = Txn_Value_Cleaner(value)
            
        elif action == "SELL":
            value = responseArray[-1]
            value = Txn_Value_Cleaner(value)
            
            #value = "SELL-------"
        else:
            value = "ERROR"
    else:
        return "SMALL RPS"
    #print(responseArray)
    return value
    



def Txn_Value_Cleaner(input_):
#Transform string to a list, has a form of xx...'.'xx....' '($xx..","..)
# Traverse list until it sees '$' save string from the following index to the end
# Remove extras and return clean float value 
#The text[1:] returns the string in text from position 1 to the end, positions count from 0 so '1' is the second character.
    list_ = list(input_)
    index = 0
    for x in list_:
        if x == '$':
            b = input_[index+1:]
            b = b.translate(str.maketrans({',': '', ')': ''}))
            return float(b)
        index += 1

        


#print("SELL EXAMPLE-------------")
#print(type(getTxnValue('0x1a0dad3ca8c0612b4828bf22677617647f7fe00d09ee4890da0f79ad23064880')))
#print(getTxnValue('0x4998f506289d95b50fb5f8bc91da0b47bd0a091ad1837e5119a9e4df55b9b049',"SELL"))
#print("ARRAY: ------------")
#print(responseArray)