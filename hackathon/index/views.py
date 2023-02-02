from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from index.forms import UploadForm
import requests
import json
import pandas as pd
from django.core.cache import caches

# cache = caches['redis']

def func(gpa, satm , sate, act):
    url = "https://www.collegedata.com/api/chances/relevant?gpa={}&satScores={}%2C{}&actCompositeScore={}&earlyApp=false".format(gpa, satm,sate, act)
    payload={}
    headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzU4NjE3NTcsImlhdCI6MTY3NTI1Njk1NywianRpIjoiNjQyNTE4NmItNTZjYy00N2VjLTk0ZjMtM2Q4NzM3MzYwOTBmIiwic2NvcGUiOiIiLCJzdWIiOiIyMDA3NzU3ODQifQ.G15sMs3QOUE9KfDwzWvWpRFjmXuflyrWiHBAwvL2oHg',
    'Cookie': 'cd_auth=%7B%22accessToken%22%3A%22eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzU4NjYxMTQsImlhdCI6MTY3NTI2MTMxNCwianRpIjoiNjNiYTc0MmYtYzllNC00MzVkLThmZjYtNTg2OWUxNmU1OTc2Iiwic2NvcGUiOiIiLCJzdWIiOiIyMDA3NzU3ODQifQ.UVODhiJLSmUrJnazvs6KDcJKGB7a3wdZz-iHdawMFHI%22%2C%22refreshToken%22%3A%22a42a13a4-cc99-470f-bc62-c776c2e4161a%22%7D'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response
   




def home(request):
    return HttpResponse("This is home")

def upload(request):
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
        gpa= form.cleaned_data.get("GPA")
        satm= form.cleaned_data.get("SATM")
        sate= form.cleaned_data.get("SATE")
        act= form.cleaned_data.get("ACT")
        response=func(gpa=gpa,satm=satm,sate=sate,act=act)

        response=response.text
        dat=json.loads(response)
        df=pd.json_normalize(dat, "likely")
                # df=df.sort("chance", axis="columns")
        df=df.drop("address.street1", axis="columns")
        df=df.drop("address.city", axis="columns")
        df=df.drop("address.state", axis="columns")
        df=df.drop("address.zipCode", axis="columns")
        df=df.sort_values(by="chance", ascending=False)
        # df.set_index('id', inplace=True)
        # df=df.to_html(classes=["table-bordered", "table-striped", "table-hover"])
        json_records = df.reset_index().to_json(orient ='records')
        arr = []
        arr = json.loads(json_records)
        contextt = {'d': arr}
        return  render(request,'Form/index.html',contextt)
        return HttpResponse(df)
    return render(request, 'Form/upload.html', {'form' : UploadForm})