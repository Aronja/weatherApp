import requests

#
# DARK_SKY_API_KEY="70573f8f45cd15ab543902b7d5540fcb"
#
# #req = requests.request('GET', 'https://api.darksky.net/forecast/0123456789abcdef9876543210fedcba/42.3601,-71.0589'+)
#
#
# response = requests.get("https://api.darksky.net/forecast/"+DARK_SKY_API_KEY)
# json_res = response.json()
# print("\n"+(d_from_date + timedelta(days=i)).strftime('%Y-%m-%d %A'))
#
#
# response = requests.get("https://api.darksky.net/forecast/"+"70573f8f45cd15ab543902b7d5540fcb"+"/"+latitude+","+longitude+","+search_date+"?"+option_list)
#     "paddington, london" 2017-08-05 2017-08-07
#

response = requests.get("https://api.darksky.net/forecast/70573f8f45cd15ab543902b7d5540fcb/37.8267,-122.4233")
print(response)
