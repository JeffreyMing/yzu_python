# 市售食米抽檢不合格產品
# https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx
# 市售食米抽檢合格產品
# https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceQualified.aspx

import json
import requests

#url = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx'
url = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceQualified.aspx'

r = requests.get(url)

#print(r.status_code)
#print(r.text)

bad_rices = json.loads(r.text)
for bad in bad_rices:
    if '月光' in bad.get('品名'):
        print(bad.get('品名'))