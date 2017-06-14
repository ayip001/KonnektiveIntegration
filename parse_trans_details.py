from credentials import credentials
import json
import urllib2
import time

# konnektive API credentials
LOGIN = credentials["API_USERNAME"]
PASS = credentials["API_PASSWORD"]

"""
parseTrans(orderType, startDate, endDate)

orderType: SALE, RECURRING etc. Run logParseTrans() to see the types
startDate, endDate: self-explainatory. mm/dd/yy string

returns a list of all transactions from startDate to endDate and raise error if
failed to parse.
"""
def parseTrans(orderType="", startDate=time.strftime("%m/%d/%Y"),
    endDate=time.strftime("%m/%d/%Y")):
    trans = []
    page = 1
    while True:
        requestURL = \
            ("https://api.konnektive.com/transactions/query/?startDate=" +
            startDate + "&endDate=" + endDate + "&resultsPerPage=200&page=" +
            str(page) + "&orderType=" + orderType + "&loginId="+ LOGIN +
            "&password=" + PASS)
        response = json.load(urllib2.urlopen(requestURL))
        # print str(requestURL)
        if response["result"] == "SUCCESS":
            trans.extend(response["message"]["data"])
        else:
            raise ValueError(response["message"])
        page += 1
        if len(trans) >= response["message"]["totalResults"]:
            return trans

"""
rebillSummaryByCampaign(campaignName, billingCycleNumber, startDate, endDate)

campaignName: find out the campaign name by running logParseTrans(). Leave
    empty for all campaigns
billingCycleNumber: self-explainatory. int
startDate, endDate: self-explainatory. mm/dd/yy string

outputs two numbers: [sucessful rebills, total rebills] within the timeframe
"""
def rebillSummaryByCampaign(campaignName, billingCycleNumber,
    startDate=time.strftime("%m/%d/%Y"), endDate=time.strftime("%m/%d/%Y")):
    total = 0
    success = 0
    trans = parseTrans("RECURRING", startDate, endDate)
    for entry in trans:
        if entry["billingCycleNumber"] == billingCycleNumber:
            if entry["campaignName"] == campaignName or campaignName == "":
                total += 1
                if entry["responseType"] == "SUCCESS":
                    success += 1
    return [success, total]

"""
parseTrans(orderType, startDate, endDate)

param: see parseTrans() docs

outputs the results from parseTrans() to log.txt for studying
"""
def logParseTrans(orderType="", startDate=time.strftime("%m/%d/%Y"),
    endDate=time.strftime("%m/%d/%Y")):
    text_file = open("log.txt", "w")
    text_file.write(json.dumps(parseTrans(orderType, startDate, endDate),
        indent=4, sort_keys=True))
    text_file.close()

print rebillSummaryByCampaign("", 3)

# print json.dumps(parseTransJson(), indent=4, sort_keys=True)

# jsonData = response["message"]["data"]
# for item in jsonData:
#     responseText = item.get("responseText")
#     orderId = item.get("orderId")
#     print responseText
#     print orderId
# parsed = json.loads(jsonData)
# print json.dumps(jsonData, indent=4, sort_keys=True)
