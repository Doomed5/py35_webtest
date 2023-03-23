import requests

url = "http://api.lemonban.com/futureloan/member/login"

params = {
    "mobile_phone": "18435132058",
    "pwd": "0987syw.."
}
header = {
    "X-Lemonban-Media-Type": "lemonban.v2"
}
response = requests.post(url=url, json=params, headers=header)
res = response.json()
print(res)
token = res['data']['token_info']['token']
print(token)
member_id = res['data']['id']

url2 = "http://api.lemonban.com/futureloan/member/recharge"
params2 = {
    'member_id': member_id,
    "amount": 400000
}
header2 = {
    "X-Lemonban-Media-Type": "lemonban.v2",
    "Authorization": "Bearer " + token
}
response2 = requests.post(url=url2,json=params2,headers=header2)
print(response2.json())
