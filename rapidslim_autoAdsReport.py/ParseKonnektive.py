import json
import urllib2

# konnektive API credentials
loginId = "angusrapidapi"
password = "moneycow"

requestURL = "https://api.konnektive.com/transactions/query/?startDate=4/10/17&endDate=4/10/17&responseType=SOFT_DECLINE&loginId=" + loginId + "&password=" + password

response = json.load(urllib2.urlopen(requestURL))

jsonData = response["message"]["data"]
for item in jsonData:
    responseText = item.get("responseText")
    orderId = item.get("orderId")
    print responseText
    print orderId
# parsed = json.loads(jsonData)
# print json.dumps(jsonData, indent=4, sort_keys=True)
