import requests
from bs4 import BeautifulSoup
import re
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value, OperatingSystem.MAC_OS_X.value]
software_names = [SoftwareName.CHROME.value,SoftwareName.FIREFOX.value]

user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=400)
user_agent = user_agent_rotator.get_random_user_agent()
print(user_agent)
headers = {"user-agent":user_agent}
url = "https://sci-hub.do"
payload = {"request": "18425907"}
with requests.session() as s:
        
        r = s.post(url, data = payload, headers = headers)
        print(r.status_code)


# class botHandler:
#     def __init__(self,token):
#         self.token = token

#     def get_update(self, offset=None):
        
#         url = "https://api.telegram.org/bot{}/Getupdates?offset={}&timeout=100".format(self.token, offset)
#         r = requests.get(url)
#         result = r.json()["result"]
        
#         return result

#     def sendMessage(self, message, chat_id):
#         url = "https://api.telegram.org/bot{}/SendMessage?chat_id={}&text={}".format(self.token, chat_id, message)
#         r = requests.get(url)
        

#     def upload(self, PMID, chat_id):
#         headers = {"user-agent":"Mozilla/5.0"}
#         url = "https://sci-hub.do"
#         payload = {"request": PMID}
#         s = requests.Session()
#         r = s.post(url, data = payload, headers = headers)
#         print(r.status_code)
#         try:
#             soup = BeautifulSoup(r.text, "html.parser")
#             result = soup.find_all("a")[0].get("onclick")
#             groups = re.search(r"//(.*)", result)
#             doc_url = groups.group(1)
            
#         except:
#             self.sendMessage("Something Went wrong, Please double check your PMID", chat_id)

#         else:
            
#             request_url = "https://api.telegram.org/bot{token}/senddocument?chat_id={id}&document={docurl}".format(token = self.token, id = chat_id, docurl = doc_url)
#             requests.get(request_url)
        


# bot = botHandler("1596209098:AAHirDlYEQsz-nKLik-Bdkv7IcK5jBqi0uI")
# update_id = 0
# while True:

#     updates = bot.get_update(update_id)
#     if updates:
#         n = len(updates) -1
#         latest_id = updates[n]["update_id"]
#         chat_id = updates[n]["message"]["chat"]["id"]
#         message = updates[n]["message"]["text"]
#         update_id = latest_id+1
#         print("message: ", message, "from", chat_id, update_id)

#         if message =="/start" or message == "/help":
#             bot.sendMessage("Please Send the PMID of the article", chat_id)

#         else:
#             bot.upload(message, chat_id)
        

#     else:
#         continue
