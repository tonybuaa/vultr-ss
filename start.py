import requests,json

api_applist = "https://api.vultr.com/v1/app/list"
response = requests.get(api_applist)
data_json = json.loads(response.text)
for app in data_json.values():
  print(app['APPID'],app['deploy_name'])

api_regionslist = "https://api.vultr.com/v1/regions/list"
response = requests.get(api_regionslist)
data_json = json.loads(response.text)
for dc in data_json.values():
  print(dc['DCID'],dc['name'],dc['country'])

api_planlist = "https://api.vultr.com/v1/plans/list?type=vc2"
response = requests.get(api_planlist)
data_json = json.loads(response.text)
for plan in data_json.values():
  print(plan['VPSPLANID'],plan['ram'],plan['price_per_month'])

api_oslist = "https://api.vultr.com/v1/os/list"
response = requests.get(api_oslist)
data_json = json.loads(response.text)
for os in data_json.values():
  print(os['OSID'],os['name'])

headers = {"API-Key":"I6VSXIJ3U4OARGCTW5F64NJLB3AWGDJC5CLA"}
# api_create_script = "https://api.vultr.com/v1/startupscript/create"
# payload = {
#   "name": "docker startup",
#   "script": "#!/bin/bash\ndocker run -dt --name ss -p 9052:9052 mritd/shadowsocks -s \"-s 0.0.0.0 -p 9052 -m chacha20-ietf-poly1305 -k 68576840 --fast-open\""
# }
# r = requests.post(api_create_script,data=payload,headers=headers)
# print(r.request.headers)
# print(r.request.body)
# print(r.content)

api_create_server = "https://api.vultr.com/v1/server/create"
payload = {
  "DCID": "25",
  "OSID": "186",
  "APPID": "37",
  "VPSPLANID": "201",
  "SCRIPTID": "340469"
}

r = requests.post(api_create_server,data=payload,headers=headers)
print(r.request.headers)
print(r.request.body)
print(r.content)
