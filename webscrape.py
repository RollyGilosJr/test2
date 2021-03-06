# import requests
# import json
# from datetime import datetime
# import pickle, os
# import base64
# from func_timeout import func_timeout, FunctionTimedOut
# 
# username = "huwanmatteo@gmail.com"  # Copyleaks Username
# apiKey = "d7b11b2f-cc6d-420f-89f7-ca4213c0cbc5"  # Copyleaks API key
# 
# 
# class CopyLeaks:
# 
#     # Initialise the CopyLeaks API service with Username and Api Key
#     def __init__(self, username, apiKey):
#         self.username = username
#         self.apiKey = apiKey
#         self.token = None
# 
#     # Function to generate token
#     def getToken(self):
#         if self.token != None:
#             content = json.loads(self.gTresponse.content)
#             dt, tm = content[".expires"][:19].split("T")
#             dt, tm = list(map(int, dt.split("-"))), list(map(int, tm.split(":")))
#             expDatetime = datetime(dt[0], dt[1], dt[2], tm[0], tm[1], tm[2])
#             if expDatetime > datetime.now():
#                 self.token = content["access_token"]
#                 return self.token
# 
#         if os.path.exists("token.p"):
#             with open("token.p", "rb") as f:
#                 self.gTresponse = pickle.load(f)
#                 content = json.loads(self.gTresponse.content)
#                 dt, tm = content[".expires"][:19].split("T")
#                 dt, tm = list(map(int, dt.split("-"))), list(map(int, tm.split(":")))
#                 expDatetime = datetime(dt[0], dt[1], dt[2], tm[0], tm[1], tm[2])
#                 if expDatetime > datetime.now():
#                     print("Last Token is Valid")
#                     self.token = content["access_token"]
#                     return self.token
# 
#         headers = {'Content-type': 'application/json'}
#         data = '{\n  "email": "' + self.username + '",\n  "key": "' + self.apiKey + '"\n}'
#         print("New Token is Generated")
#         self.gTresponse = requests.post('https://id.copyleaks.com/v3/account/login/api', headers=headers, data=data)
#         with open("token.p", "wb") as f:
#             pickle.dump(self.gTresponse, f)
#         content = json.loads(self.gTresponse.content)
#         self.token = content["access_token"]
#         return self.token
# 
#     # Function to get available credit balance
#     def getCreditBalance(self):
#         headers = {'Authorization': 'Bearer ' + self.getToken()}
#         self.gCresponse = requests.get('https://api.copyleaks.com/v3/education/credits', headers=headers)
#         balance = json.loads(self.gCresponse.content)["Amount"]
#         return balance
# 
#     # Fuction to show last 2 months usage history
#     def getLastHistory(self):
#         today = datetime.today()
#         headers = {'Authorization': 'Bearer ' + self.getToken()}
#         self.gHresponse = requests.get(
#             'https://api.copyleaks.com/v3/education/usages/history?start=01-{2}-{1}&end=30-{0}-{1}'.format(today.month,
#                                                                                                            today.year,
#                                                                                                            today.month - 1),
#             headers=headers)
#         content = "\n".join(["\t\t".join(line.split(",")) for line in self.gHresponse.content.decode().split("\n")])
#         print(content)
#         return self.gHresponse.content.decode()
# 
#     # Function to generate Base64 String from file
#     def getBase64(self, file):
#         with open(file, "rb") as file:
#             encoded = base64.b64encode(file.read())
#             return encoded.decode()
# 
#     # Function to submit file to Copyleaks and start to generate report
#     def submitFile(self, filePath, customID):
# 
#         base64str = self.getBase64(filePath)
#         headers = {'Content-type': 'application/json', 'Authorization': 'Bearer ' + self.getToken()}
#         data = '{\n  "base64": "%s",\n  "filename": "%s",\n  "properties": {\n "pdf" : {\n "create" : true, \n "title" : "%s" \n }, \n  "webhooks": {\n  "status": "https://yoursite.com/webhook/{STATUS}/%s"\n}\n}\n}' % (
#         base64str, os.path.basename(filePath), customID, customID)
#         print(data)
#         self.gFresponse = requests.put('https://api.copyleaks.com/v3/education/submit/file/{}'.format(customID),
#                                        headers=headers, data=data)
# 
#         return self.gFresponse
# 
#     # Function to get/save report pdf
#     def getPDFreport(self, customID, savePath=None):
#         headers = {'Authorization': 'Bearer ' + self.getToken()}
#         self.gPresponse = requests.get('https://api.copyleaks.com/v3/downloads/{}/report.pdf'.format(customID),
#                                        headers=headers)
#         if savePath and self.gPresponse.status_code == 200:
#             with open(savePath, "wb") as f:
#                 f.write(self.gPresponse.content)
#                 return self.gPresponse
#         return self.gPresponse
# 
#     # Function to give the status of the ID
#     def getStatus(self, customID, filePath=None):
# 
#         submittedIDs = [c.split(",")[1][1:-1] for c in self.getLastHistory().split("\n")[1:-1]]
#         if str(customID) in submittedIDs:
#             try:
#                 if filePath:
#                     _ = func_timeout(5, self.getPDFreport, args=(customID, filePath))
#                     return "Generated"
#                 else:
#                     _ = func_timeout(5, self.getPDFreport, args=(customID,))
#             except FunctionTimedOut:
#                 return "Generating"
# 
#         else:
#             return "Not Generated"
# 
# 
# test = CopyLeaks(username, apiKey)
# # print(test.submitFile("c.pdf",1))
# print(test.getStatus(1))


# https://www.prepostseo.com/frontend/checkPlagv5

# query-list: Best Plagiarism Detector Online Unique Content Checker tool for checking articles, essays & website content are they are unique or not our Duplicate conten


import requests

url = ('https://www.prepostseo.com/plagiarism-checker')

payload = {
    'query-list': 'Best Plagiarism Detector Online Unique Content Checker tool for checking articles, essays & website content are they are unique or not our Duplicate conten'
}

r = requests.get(url,data=payload)

print(r.text)