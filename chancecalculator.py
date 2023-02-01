import requests
import json
import pandas as pd

# we will get the input values fromt the form
gpa=4
weightedgpa=4
satscorem=400
satscoree=400
actscore=24


url = "https://www.collegedata.com/api/auth/login"

payload='username=dstablet55%40gmail.com&password=Ds%408005314216'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

response=response.text
df=json.loads(response)
token=df['accessToken']
print(token)




url = "https://www.collegedata.com/api/chances/relevant?gpa={}&weightedGpa=4&satScores={}%2C{}&actCompositeScore={}&earlyApp=false".format(gpa, satscoree,satscorem, actscore)

payload={}
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzU4NjE3NTcsImlhdCI6MTY3NTI1Njk1NywianRpIjoiNjQyNTE4NmItNTZjYy00N2VjLTk0ZjMtM2Q4NzM3MzYwOTBmIiwic2NvcGUiOiIiLCJzdWIiOiIyMDA3NzU3ODQifQ.G15sMs3QOUE9KfDwzWvWpRFjmXuflyrWiHBAwvL2oHg',
  'Cookie': 'cd_auth=%7B%22accessToken%22%3A%22eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzU4NjYxMTQsImlhdCI6MTY3NTI2MTMxNCwianRpIjoiNjNiYTc0MmYtYzllNC00MzVkLThmZjYtNTg2OWUxNmU1OTc2Iiwic2NvcGUiOiIiLCJzdWIiOiIyMDA3NzU3ODQifQ.UVODhiJLSmUrJnazvs6KDcJKGB7a3wdZz-iHdawMFHI%22%2C%22refreshToken%22%3A%22a42a13a4-cc99-470f-bc62-c776c2e4161a%22%7D'
}
response = requests.request("GET", url, headers=headers, data=payload)
response=response.text
dat=json.loads(response)
df=pd.json_normalize(dat, "likely")
print(df)


