# NOTE: THIS ONLY WORKS FOR MY CAMPAIGN. MODIFY THE THIRD PARAMETER OF
# parse_trans_details.getRebillSummaryByCampaign() TO SUIT YOUR OWN CAMPAIGNS

import parse_trans_details
from datetime import date, timedelta

d = raw_input('please enter a date mm/dd/yyyy or leave it blank for yesterday:\n')
if d == '':
    d = (date.today() - timedelta(1)).strftime("%m/%d/%Y")

print "Parsing for " + d
parsed = parse_trans_details.parseTrans(d, d)
# parsed = parse_trans_details.parseTransFromLog() # FOR TESTING ONLY

print "\nTotal"
print "\nRebill Summary"
temp = parse_trans_details.getRebillSummaryByCampaign(parsed, 2)
print "1st Rebill: " + str(temp[0]) + " of " + str(temp[1])
temp = parse_trans_details.getRebillSummaryByCampaign(parsed, 3)
print "2nd Rebill: " + str(temp[0]) + " of " + str(temp[1])
temp = parse_trans_details.getRebillSummaryByCampaign(parsed, 4)
print "3rd Rebill: " + str(temp[0]) + " of " + str(temp[1])
temp = parse_trans_details.getRebillSummaryByCampaign(parsed, range(5,15))
print "add Rebill: " + str(temp[0]) + " of " + str(temp[1])

print "\nRecycle Summary"
temp = parse_trans_details.getRecycleSummaryByCampaign(parsed, 1)
print "1st Recycle: " + str(temp[0]) + " of " + str(temp[1])
temp = parse_trans_details.getRecycleSummaryByCampaign(parsed, 2)
print "2nd Recycle: " + str(temp[0]) + " of " + str(temp[1])
temp = parse_trans_details.getRecycleSummaryByCampaign(parsed, 3)
print "3rd Recycle: " + str(temp[0]) + " of " + str(temp[1])
temp = parse_trans_details.getRecycleSummaryByCampaign(parsed, range(4,15))
print "add Recycle: " + str(temp[0]) + " of " + str(temp[1])



print "\nBioleans"
print "\nRebill Summary"
temp = parse_trans_details.getRebillSummaryByCampaign(parsed, 2, 'Biolean Lander')
print "1st Rebill: " + str(temp[0]) + " of " + str(temp[1])
temp = parse_trans_details.getRebillSummaryByCampaign(parsed, 3, 'Biolean Lander')
print "2nd Rebill: " + str(temp[0]) + " of " + str(temp[1])
temp = parse_trans_details.getRebillSummaryByCampaign(parsed, 4, 'Biolean Lander')
print "3rd Rebill: " + str(temp[0]) + " of " + str(temp[1])
temp = parse_trans_details.getRebillSummaryByCampaign(parsed, range(5,15), 'Biolean Lander')
print "add Rebill: " + str(temp[0]) + " of " + str(temp[1])

print "\nRecycle Summary"
temp = parse_trans_details.getRecycleSummaryByCampaign(parsed, 1, 'Biolean Lander')
print "1st Recycle: " + str(temp[0]) + " of " + str(temp[1])
temp = parse_trans_details.getRecycleSummaryByCampaign(parsed, 2, 'Biolean Lander')
print "2nd Recycle: " + str(temp[0]) + " of " + str(temp[1])
temp = parse_trans_details.getRecycleSummaryByCampaign(parsed, 3, 'Biolean Lander')
print "3rd Recycle: " + str(temp[0]) + " of " + str(temp[1])
temp = parse_trans_details.getRecycleSummaryByCampaign(parsed, range(4,15), 'Biolean Lander')
print "add Recycle: " + str(temp[0]) + " of " + str(temp[1])



print "\nRapid Slim"
print "\nRebill Summary"
temp = parse_trans_details.getRebillSummaryByCampaign(parsed, 2, 'Rapid Lander')
print "1st Rebill: " + str(temp[0]) + " of " + str(temp[1])
temp = parse_trans_details.getRebillSummaryByCampaign(parsed, 3, 'Rapid Lander')
print "2nd Rebill: " + str(temp[0]) + " of " + str(temp[1])
temp = parse_trans_details.getRebillSummaryByCampaign(parsed, 4, 'Rapid Lander')
print "3rd Rebill: " + str(temp[0]) + " of " + str(temp[1])
temp = parse_trans_details.getRebillSummaryByCampaign(parsed, range(5,15), 'Rapid Lander')
print "add Rebill: " + str(temp[0]) + " of " + str(temp[1])

print "\nRecycle Summary"
temp = parse_trans_details.getRecycleSummaryByCampaign(parsed, 1, 'Rapid Lander')
print "1st Recycle: " + str(temp[0]) + " of " + str(temp[1])
temp = parse_trans_details.getRecycleSummaryByCampaign(parsed, 2, 'Rapid Lander')
print "2nd Recycle: " + str(temp[0]) + " of " + str(temp[1])
temp = parse_trans_details.getRecycleSummaryByCampaign(parsed, 3, 'Rapid Lander')
print "3rd Recycle: " + str(temp[0]) + " of " + str(temp[1])
temp = parse_trans_details.getRecycleSummaryByCampaign(parsed, range(4,15), 'Biolean Lander')
print "add Recycle: " + str(temp[0]) + " of " + str(temp[1])
