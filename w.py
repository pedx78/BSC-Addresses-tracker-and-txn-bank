import requests
from bs4 import BeautifulSoup
#https://bscscan.com/address/0xcC64ea842FcDe4283CF239259f7462Ef809c44FD

def getTokenBalance(whale):
    url = "https://bscscan.com/address/" + whale
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    getId = soup.find(id='availableBalanceDropdown')
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
    return final

#print(getTokenBalance("0xcC64ea842FcDe4283CF239259f7462Ef809c44FD"))

#0xcc64ea842fcde4283cf239259f7462ef809c44fd
#0x1a0dad3ca8c0612b4828bf22677617647f7fe00d09ee4890da0f79ad23064880

responseArray = []
def getTxnValue(hash, action):
    url = "https://bscscan.com/tx/" + hash
    #webbrowser.open(url, new=2)
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    #getId = soup.find(id='availableBalanceDropdown')
    #results = getId.text

    results = soup.find_all('span', class_='mr-1')
    #results1 = results.find_all(attrs={"data-toggle": "tooltip"})
    #print("NEXT")
    #done = extra[0].text
    index = 0
    
    for result in results:
        a = results[index].find_all(attrs={"data-toggle": "tooltip"})
        index += 1
        #print(result)
        #print("Solution: ---------------------------")
        if a != []:
            #print(type(a))
            #print(a[0].text)
            #print(type(a[0].text))
            responseArray.append(a[0].text)
            print(responseArray)
    '''
    if action == "BUY":
        value = responseArray[1]
        value = Txn_Value_Cleaner(value)
    elif action == "SELL":
        value = responseArray[-1]
        value = Txn_Value_Cleaner(value)
    else:
        value = "ERROR"
        '''
    
    return responseArray



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
print(getTxnValue('0x87e296cab36467a7d7f84a509d2609b4fc9e49984d1ca8c47bf0d827dd83a3e0', "BUY"))
#print("ARRAY: ------------")
#print(responseArray)