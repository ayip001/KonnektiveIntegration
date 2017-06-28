import parse_trans_details

parsed = parse_trans_details.parseTransFromLog()
print parse_trans_details.getRecycleSummaryByCampaign(parsed, 1)
# print parse_trans_details.getRefundsAmtByCampaign(parsed)
